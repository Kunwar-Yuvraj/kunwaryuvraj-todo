from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('task-list', TaskList.as_view(template_name='task-list.html'), name='task-list'),
    path('', index, name='index'),
    path('login', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='index'), name='logout'),
    path('register', RegisterPage.as_view(template_name='register.html'), name='register'),
    path('task-create', TaskCreate.as_view(template_name='task-create.html'), name='task-create'),
    path('task-detail/<int:pk>', TaskDetail.as_view(template_name='task-detail.html'), name='task-detail'),
    path('task-delete/<int:pk>', TaskDelete.as_view(template_name='task-delete.html'), name='task-delete'),
    path('task-update/<int:pk>', TaskUpdate.as_view(template_name='task-update.html'), name='task-update'),
]
