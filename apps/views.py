from django.shortcuts import redirect, render
from .models import TodoModel

# Create your views here.
def todoview(request):
    mytodo = TodoModel.objects.all()
    context = {'mytodos': mytodo }
    return render(request, "todoapp/homepage.html", context)

def addtask(request):
    # write a coe to add the input data to the database
    mytask = request.POST['task']
    TodoModel(task = mytask).save()
    return redirect(request.META['HTTP_REFERER'])

def deletetask(request, taskpk):
    # write a code to delete the task
    TodoModel.objects.filter(id = taskpk).delete()
    return redirect(request.META['HTTP_REFERER'])


def edittaskview(request, taskpk):
    # write a code to view the edit fields
    context = {"todopk":taskpk}
    return render(request, "todoapp/edittask.html", context)

def edittask(request, taskpk):
    userenteredtask = request.POST['task']
    todo = TodoModel.objects.filter(id = taskpk)[0]
    todo.task = userenteredtask
    todo.save()
    return redirect('homepage')











