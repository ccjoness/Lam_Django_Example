from django.shortcuts import render
from django.http import HttpResponse
from todo_app.models import ToDoList
from django.shortcuts import get_object_or_404


def home_page_view(request):
    return HttpResponse('ok')


def list_view(request):
    all_lists = ToDoList.objects.all()
    for li in all_lists:
        print(li.first_char())
    return render(request, 'all_lists.html', {'all_lists': all_lists})


def single_view(request, pk):
    # single_list = ToDoList.objects.get(pk=pk)
    single_list = get_object_or_404(ToDoList, pk=pk)
    return render(request, 'single_list.html', {'single_list': single_list})
