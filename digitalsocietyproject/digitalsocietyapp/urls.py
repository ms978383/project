"""digitalsocietyproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.login,name="login"),
    path('digitalsociety/home/',views.home,name="home"),
    path('digital-society/logout/',views.logout,name="logout"),
    path('digital-society/dashboard/profile/',views.profile,name="profile"),
    path('digital-society/dashboard/profile/user-pic-change/',views.user_pic_change,name="user-pic-change"),
    path('digital-society/dashboard/profile/account-details/password-change/',views.password_change,name="password-change"),
    path('digital-society/dashboard/profile/account-details/user-details-change/',views.user_details_change,name="user-deatils-change"),
    path('digital-society/dashboard/add-society-member/',views.add_society_member,name="add-society-member"),
    path('digital-society/dashboard/all-society-member/',views.all_society_member,name="all-society-member"),
    path('digital-society/dashboard/all-society-member/edit/<int:id>/',views.edit_member,name="edit-member"),
    path('digital-society/dashboard/all-society-member/edit/update-member/',views.update_member,name="update-member"),
    path('digital-society/dashboard/add-notice/',views.add_notice,name="add-notice"),
    path('digital-society/dashboard/all-society-notice/',views.all_society_notice,name="all-society-notice"),
    path('digital-society/dashboard/all-society-notice/edit/<int:id>/',views.edit_notice,name="edit-notice"),
    path('digital-society/dashboard/all-society-notice/edit/update-notice/',views.update_notice,name="update-notice"),
    path('digital-society/dashboard/add-event/',views.add_event,name="add-event"),
    path('digital-society/dashboard/all-society-event/',views.all_society_event,name="all-society-event"),
    path('digital-society/dashboard/all-society-event/edit/<int:id>/',views.edit_event,name="edit-event"),
    path('digital-society/dashboard/all-society-event/edit/update-event/',views.update_event,name="update-event"),
    path('digital-society/dashboard/all-society-member/delete/<int:id>/',views.delete_member,name="delete-member"),
    path('digital-society/dashboard/all-society-notice/delete/<int:id>/',views.delete_notice,name="delete-notice"),
    path('digital-society/dashboard/all-society-event/delete/<int:id>/',views.delete_event,name="delete-event"),
    path('digital-society/register/',views.register,name="register"),
    path('digital-society/dashboard/all-user-id-password/',views.all_user_id_password,name="all-user-id-password"),
    path('digital-society/forgot-password/',views.forgot_password,name="forgot-password"),
]
