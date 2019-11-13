from django.urls import path
from todo_app import views

app_name = 'todo_app'

urlpatterns = [
    path('list/', views.list_view, name='home'),
    path('single/<int:pk>', views.single_view, name='single_view'),
]
