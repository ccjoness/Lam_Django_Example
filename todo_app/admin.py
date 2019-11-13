from django.contrib import admin

from todo_app.models import ToDoList, Item

admin.site.register(ToDoList)
admin.site.register(Item)
