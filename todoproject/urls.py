from django.contrib import admin
from django.urls import path, include
from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_todo_items, name='list_todo_items'),
    path('insert_todo/', views.insert_todo_item, name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/', views.delete_todo_item, name="delete_todo_item"),
    # path('', home, name="home"),  # Uncomment if home view exists
    # path('todos/', include('todos.urls')),  # Uncomment if using separate URLs for 'todos' app
]
