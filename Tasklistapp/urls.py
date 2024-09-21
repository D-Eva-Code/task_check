from django.urls import path
from Tasklistapp import views


urlpatterns = [
    path('', views.todolist, name="todolist" ),
    path('delete/<task_id>', views.delete, name="delete" ),
    path('edit/<task_id>', views.edit, name="edit" ),
    path('completed/<task_id>', views.completed, name="completed" ),
    path('pending/<task_id>', views.pending, name="pending" ),
   
]