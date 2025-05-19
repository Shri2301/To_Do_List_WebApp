from django.contrib import admin
from django.urls import path
from authapp.views import user_signup, user_login, user_logout, user_reset_pass, user_otp1, user_otp2
from tdapp.views import home, create_task, view_task, delete_task, cross_off, uncross, edit_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("user_signup", user_signup, name="user_signup"),
    path("user_login", user_login, name="user_login"),
    path("user_logout", user_logout, name="user_logout"),
    path("user_otp1", user_otp1, name="user_otp1"),
    path("user_otp2", user_otp2, name="user_otp2"),
    path("user_reset_pass", user_reset_pass, name="user_reset_pass"),
    path("create_task", create_task, name="create_task"),
    path("view_task", view_task, name="view_task"),
    path("delete_task/<int:id>", delete_task, name="delete_task"),
    path("cross_off/<int:id>", cross_off, name="cross_off"),
    path("uncross/<int:id>", uncross, name="uncross"),
    path("edit_task/<int:id>", edit_task, name="edit_task"),
]
