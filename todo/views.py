from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import task
from .forms import TaskForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:home')
    else:
        form = TaskForm()
    
    tasks = task.objects.all().order_by('completed', '-date')
    pending_count = task.objects.filter(completed=False).count()
    return render(request, 'home.html', {'tasks': tasks, 'form': form, 'pending_count': pending_count})

def edit_task(request, task_id):
    item = get_object_or_404(task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo:home')
    else:
        form = TaskForm(instance=item)
    return render(request, 'edit.html', {'form': form, 'task': item})

def delete_task(request, task_id):
    item = get_object_or_404(task, id=task_id)
    item.delete()
    return redirect('todo:home')

def toggle_task(request, task_id):
    item = get_object_or_404(task, id=task_id)
    item.completed = not item.completed
    item.save()
    return redirect('todo:home')

def about(request):
    return render(request, 'about.html')
    
def contact(request):
    return render(request, 'contact.html')
    
def analytics(request):
    all_tasks = task.objects.all()
    total = all_tasks.count()
    completed = all_tasks.filter(completed=True).count()
    pending = total - completed
    rate = round((completed / total * 100), 1) if total > 0 else 0
    
    high_priority = all_tasks.filter(priority='high').count()
    medium_priority = all_tasks.filter(priority='medium').count()
    low_priority = all_tasks.filter(priority='low').count()
    
    context = {
        'total': total,
        'completed': completed,
        'pending': pending,
        'rate': rate,
        'high': high_priority,
        'medium': medium_priority,
        'low': low_priority,
    }
    return render(request, 'analytics.html', context)
    
def focus(request):
    return render(request, 'focus.html')
    
