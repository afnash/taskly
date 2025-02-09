from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #path('',views.home_page),
    path('list/', views.list_todo_items),
    path('insert_todo',views.insert_todo_item,name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/',views.delete_todo_item,name="delete_todo_item"),
]
