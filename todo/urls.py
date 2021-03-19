from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoApp, name='TodoApp'),
    path('taskEdit/<int:pk>', views.TaskEdit, name='taskEdit'),
    path('taskDelete/<int:pk>', views.TaskDelete, name='taskDelete'),
]