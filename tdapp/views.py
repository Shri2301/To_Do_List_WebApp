from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import TaskModel
from .forms import TaskForm
from django.contrib import messages

def home(request):
	if request.user.is_authenticated:
		return render(request, "home.html")
	else:
		return redirect( "user_login")	

def create_task(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			fm = TaskForm(request.POST or None)
			if fm.is_valid():
				task = fm.save(commit=False)
				task.user = request.user
				task.save()
				fm = TaskForm()
				messages.success(request, "Your Task has been added to the list")
				return render(request, "create_task.html", {"fm":fm})
		else:
			fm = TaskForm()
			return render(request, "create_task.html", {"fm":fm})	

def edit_task(request, id):
	if request.user.is_authenticated:
		if request.method == "POST":
			data = TaskModel.objects.get(id=id)
			fm = TaskForm(request.POST or None, instance=data)
			if fm.is_valid():
				fm.save()
				messages.success(request, "Your Task has been Edited")
				return redirect("view_task")
		else:
			data = TaskModel.objects.get(id=id)
			return render(request, "edit_task.html", {"data":data})

def view_task(request):
	if request.user.is_authenticated:
		data = TaskModel.objects.filter(user=request.user)
		return render(request, "view_task.html", {"data":data})
	else:
		return redirect("user_login")


def view_task(request):
	if request.user.is_authenticated:
		data = TaskModel.objects.filter(user=request.user)
		return render(request, "view_task.html", {"data":data})
	else:
		return redirect("user_login")

def delete_task(request, id):
	task = TaskModel.objects.get(id=id)
	task.delete()
	messages.success(request, "Task has been deleted")
	return redirect("view_task")

def cross_off(request, id):
	task = TaskModel.objects.get(id=id)
	task.status = True
	task.save()
	return redirect("view_task")

def uncross(request, id):
	task = TaskModel.objects.get(id=id)
	task.status = False
	task.save()
	return redirect("view_task")
	
"""
def edit_task(request, id):
	if request.user.is_authenticated:
		print(request.user)
		if request.method == "POST":
			data = TaskModel.objects.get(id=id)
			print(data.user, data.task, data.status)
			fm = TaskForm(request.POST, instance=data)
			if fm.is_valid():
				task = fm.save(commit=False)
				task.user = request.user
				task.save()
				messages.success(request, "Your Task has been Edited")
				return redirect("view_task")
			else:
				print("error")
				return redirect("view_task")
	
		else:
			fm = TaskForm()
			data = TaskModel.objects.get(id=id)
			return render(request, "edit_task.html", {"data":data, "fm":fm})
"""	