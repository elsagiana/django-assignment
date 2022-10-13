from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.core import serializers
from todolist.models import Task
from todolist.forms import TaskForm

# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user = request.user
    data_todolist = Task.objects.filter(user= request.user).all()
    context = {
        'data_todolist':data_todolist,
        'user':user
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user=User.objects.get(username=request.user.username)
            task.save()
            return redirect('todolist:show_todolist')

    context = {'form':form}
    return render(request, 'create_task.html', context)    

def delete(request, id):
    context = {}
    task = Task.objects.filter(pk=id)
    if request.method == "POST":
        task.delete()
        return redirect('todolist:show_todolist')

    return render(request, 'delete.html', context)    

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Berhasil membuat akun!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def todolist_json(request):
    data_todolist = Task.objects.filter(user=request.user).all()
    return HttpResponse(serializers.serialize("json", data_todolist), content_type="application/json")

@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request, "todolist_ajax.html", context)

@login_required(login_url='/todolist/login/')
def add_task_ajax(request: HttpRequest):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        new_task =  Task(
            title = title,
            description = description,
            user = request.user,
            date = datetime.now(),
        )
        new_task.save()
        return HttpResponse(serializers.serialize("json", [new_task]), content_type='application/json')
