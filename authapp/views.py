from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from random import randrange
from td_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages
from .models import OtpModel

def user_signup(request):
	if request.method == "POST":
		un = request.POST.get("un")
		em = request.POST.get("em")
		pw1 = request.POST.get("pw1")
		pw2 = request.POST.get("pw2")
		try:
			usr = User.objects.get(username=un)
			messages.success(request, "Username already exists")
			return render(request, "user_signup.html")
		except User.DoesNotExist:
			try:
				usr = User.objects.get(email=em)
				messages.success(request, "Email id already exists")
				return render(request, "user_signup.html")
			except User.DoesNotExist:
				if pw1 == pw2:
					if len(pw1) < 6:
						messages.success(request, "Too weak password")
						return render(request, "user_signup.html")
					else:
						try:	
							usr = OtpModel.objects.get(username=un)
							otp = usr.otp
						except OtpModel.DoesNotExist:				
							otp = ""
							text = "0123456789"
							for i in range(6):
								otp += text[randrange(len(text))]
						finally:
							send_mail("Welcome " + un + " to Shri's Django Website", "Your otp is " + str(otp), EMAIL_HOST_USER, [em])
							usr = OtpModel(otp=otp, username=un, email=em, password=pw1)
							usr.save()
							messages.success(request, "Otp is sent on the email id")
							return redirect("user_otp1")

				else:
					messages.success(request, "Passwords don't match")	
					return render(request, "user_signup.html")
	else:
		return render(request, "user_signup.html")

def user_login(request):
	if request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		usr = authenticate(username=un, password=pw)
		if usr is None:
			messages.success(request, "Invalid Username or Password")
			return render(request, "user_login.html")
		else:
			login(request, usr)
			return redirect("home")
	else:
		return render(request, "user_login.html")

def user_logout(request):
	logout(request)
	return redirect("user_login")

def user_reset_pass(request):
	if request.method == "POST":
		un = request.POST.get("un")
		em = request.POST.get("em")
		pw1 = request.POST.get("pw1")
		pw2 = request.POST.get("pw2")
		if pw1 == pw2:
			if len(pw1) < 6:
				messages.success(request, "Too weak password")
				return render(request, "user_signup.html")
			else:
				try:
					usr = User.objects.get(username=un) and User.objects.get(email=em)
					obj = OtpModel.objects.get(username=un)
					otp = int(obj.otp)
					send_mail("Welcome " + un + " to Shri's Django Website", "Your otp is " + str(otp), EMAIL_HOST_USER, [em])
					messages.success(request, "Otp is sent on the email id")
					return redirect("user_otp2")

				except User.DoesNotExist:
					messages.success(request, "Invalid Details")
					return render(request, "user_reset_password.html")
				except OtpModel.DoesNotExist:
					otp = ""
					text = "0123456789"
					for i in range(6):
						otp += text[randrange(len(text))]
					obj = OtpModel(otp=otp, username=un, email=em, password=pw1)
					obj.save()
					send_mail("Welcome " + un + " to Shri's Django Website", "Your otp is " + str(otp), EMAIL_HOST_USER, [em])
					messages.success(request, "Otp is sent on the email id")
					return redirect("user_otp2")
		else:
			messages.success(request, "Password don't match")
			return render(request, "user_reset_password.html")
	else:
		return render(request, "user_reset_password.html")

def user_otp1(request):
	if request.method == "POST":
		uotp = request.POST.get("uotp")
		if uotp.isnumeric():
			try:
				obj = OtpModel.objects.get(otp=uotp)
				otp = obj.otp
				un = obj.username
				em = obj.email
				pw = obj.password
				usr = User.objects.create_user(username=un, password=pw, email=em)
				usr.save()
				obj.delete()
				return redirect("user_login")
			except OtpModel.DoesNotExist:
				messages.success(request, "Invalid Otp")
				return render(request, "user_otp.html")
		else:
			messages.success(request, "Invalid Otp")
			return render(request,"user_otp.html")
	else:
		return render(request,"user_otp.html")

def user_otp2(request):
	if request.method == "POST":
		uotp = request.POST.get("uotp")
		if uotp.isnumeric():
			try:
				obj = OtpModel.objects.get(otp=uotp)
				otp = obj.otp
				un = obj.username
				em = obj.email
				pw = obj.password					
				usr = User.objects.get(username=un)
				usr.set_password(pw)
				usr.save()
				obj.delete()
				return redirect("user_login")
			except OtpModel.DoesNotExist:
				messages.success(request, "Invalid Otp")
				return render(request, "user_otp.html")
		else:
			messages.success(request, "Invalid Otp")
			return render(request,"user_otp.html")
	else:
		return render(request,"user_otp.html")
