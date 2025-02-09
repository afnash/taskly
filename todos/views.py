from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Todo

def list_todo_items(request):
    context = {'todo_list': Todo.objects.all()}
    return render(request, 'todos/todo_list.html', context)

def home(request):
    return HttpResponse("Welcome to Taskly!")

def insert_todo_item(request: HttpRequest):
    content = request.POST.get('content', '').strip()
    if content:  # Prevent saving empty todos
        todo = Todo(content=content)
        todo.save()
    return redirect('list_todo_items')

def delete_todo_item(request, todo_id):
    todo_to_delete = get_object_or_404(Todo, id=todo_id)
    todo_to_delete.delete()
    return redirect('list_todo_items')
