"""PCS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from PCS_system.views import (index, login, register, register_submit, login_submit, logout, project_submit, delete_project, edit_project, 
    project_details, update_project, view_profile, view_projects, profile_update, project_info, user_info, delete_user, role_submit, add_user,
    manage_role, change_user_role)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login),
    path('index', index),
    path('', login),
    path('register', register),
    path('register_submit', register_submit),
    path('login_submit', login_submit),
    path('logout', logout),
    path('project_submit', project_submit),
    path('delete_project/<int:project_id>', delete_project),
    path('edit_project/<int:project_id>', edit_project),
    path('project_details/<int:project_id>', project_details),
    path('project_update/<int:project_id>', update_project),
    path('profile/<int:user_id>', view_profile),
    path('view_projects', view_projects),
    path('profile_update/<int:user_id>', profile_update),
    path('project_info', project_info),
    path('user_info', user_info),
    path('delete_user/<int:user_id>', delete_user),
    path('role_submit', role_submit),
    path('add_user', add_user),
    path('manage_role', manage_role),
    path('change_user_role/<int:user_id>', change_user_role),
]
