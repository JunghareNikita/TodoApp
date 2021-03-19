from django.shortcuts import render, redirect
from todo.models import Task
from todo.forms import TaskForm

def TodoApp(request):
    list = Task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'index.html', {'form':form, 'list':list})

def TaskEdit(request, pk):
    item = Task.objects.get(id=pk)
    form = TaskForm(instance=item)
    if request.method =="POST":
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'index.html', {'form':form})

def TaskDelete(request, pk):
    if request:
        item = Task.objects.get(id=pk)
        item.delete()
        return redirect('/')
    return render(request, 'index.html')