from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Alltask
from .forms import TodoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":
        task_name = request.POST.get('task', '')  # Get the task name from the POST data
        if task_name:  # Check if the task name is not empty
            new_task = Alltask(task=task_name)
            new_task.owner=request.user
            new_task.save()
        messages.success(request, 'Task successfully added!')   
        return redirect("todolist")
    else:
        
        altask = Alltask.objects.filter(owner=request.user)
        altask = Alltask.objects.all().order_by('id')# Order the tasks by 'id'
        paginator = Paginator(altask,5)# sections the table or number of items in each page to be 5 and then continue from the next page
        page = request.GET.get('pg')# get the page number
        altask= paginator.get_page(page)# get the tasks for the current page
        
        return render(request, "todolist.html", {"context": altask} )

@login_required   
def delete (request,task_id):
    tasks = Alltask.objects.get(pk= task_id)
    if tasks.owner==request.user:
        tasks.delete()
    else:
        messages.error(request, 'Access Restricted!') 
    return redirect("todolist")

@login_required
def edit (request,task_id):
    if request.method == "POST":
        new_edit = Alltask.objects.get(pk = task_id)
        form = TodoForm(request.POST, instance=new_edit)
        if form.is_valid():
            form.save()
       
      
        messages.success(request, 'Task successfully edited!')   
        return redirect("todolist")
    else:
        
        new_task = Alltask.objects.get(pk = task_id)
        return render(request, "edit.html", {"new_task": new_task} )
    
def completed (request,task_id):
    completed_tasks = Alltask.objects.get(pk= task_id)
    if completed_tasks.owner==request.user:
        completed_tasks.done = True
        completed_tasks.save()
    else:
        messages.error(request, 'Access Restricted!')
    return redirect("todolist")

def pending (request,task_id):
    pending_tasks = Alltask.objects.get(pk= task_id)
    if pending_tasks.owner==request.user:
        pending_tasks.done = False
        pending_tasks.save()
    else:
        messages.error(request, 'Access Restricted!')
    return redirect("todolist")

def index (request):
    return render(request, "index.html", {"index":" Welcome to index page"} )


def contact (request):
    return render(request, "contact us.html", {"contact":"Contact us"} )


def about (request):
    return render(request, "about us.html", {"about":"About us"} )