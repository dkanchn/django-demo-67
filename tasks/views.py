from django.shortcuts import render # type: ignore

# Create your views here.
tasks = ["foo", "bar", "sth"]


def add(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            tasks.appe
    return render(request, "tasks/add.html")