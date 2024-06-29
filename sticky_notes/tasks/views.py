


from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

def task_list(request): 
    tasks = Task.objects.all()
    
    context = {
        'tasks': tasks,
        'page_title': 'List of Tasks'
    }
    
    return render(request, 'tasks/task_list.html', context)

def task_detail(request, pk): 
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_create(request): 
    if request.method == 'POST': 
        form = TaskForm(request.POST)
        if form.is_valid(): 
            task = form.save(commit=False)
            if request.user.is_authenticated: 
                task.author = request.user
            task.save()
            return redirect('task_list')
    else: 
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form':form})

def task_update(request, pk): 
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST": 
        form = TaskForm(request.POST, instance=task)
        if form.is_valid(): 
            task = form.save(commit=False)
            task.save()
            return redirect('task_list')
    else: 
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_update.html', {'form':form})

def task_delete(request, pk): 
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')
