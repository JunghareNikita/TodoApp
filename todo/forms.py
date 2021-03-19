from django.forms import forms, ModelForm
from todo.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task']