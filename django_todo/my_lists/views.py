from django.shortcuts import render, redirect
from .models import ToDoList

# Create your views here.


def home(request):
    lists = ToDoList.objects.all()
    return render(request, "lists.html", context={"lists": lists})


def items_list(request, pk):
    the_list = ToDoList.objects.get(pk=pk)
    items = the_list.todoitem_set.all()

    if request.method == "GET":
        return render(request, "items.html", context={"items": items})

    if request.method == "POST":
        completed_items = request.POST.getlist("checkbox")
        for item in items:
            if str(item.pk) in completed_items:
                item.is_completed = True
            else:
                item.is_completed = False

            item.save()

        return redirect("items_list", pk)
