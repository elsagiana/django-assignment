from django.urls import path
from todolist.views import show_todolist, create_task, register, login_user, logout_user, delete, todolist_json, show_todolist_ajax, add_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_task, name='create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete/<int:id>', delete, name='delete'),
    path('json/', todolist_json, name='todolist_json'),
    path('ajax/', show_todolist_ajax, name='show_todolist_ajax'),
    path('add/', add_task_ajax, name='add_task_ajax')
]