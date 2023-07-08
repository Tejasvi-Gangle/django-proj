from django.shortcuts import render,redirect,get_object_or_404
from todo.models import Todo
from todo.forms import TodoForm,ContactForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
@login_required
def contact(request):
    contactform=ContactForm(request.POST or None)
    if contactform.is_valid():
        contactform.save()
        return redirect("todolist")
    return render(request,"contact.html",{'forms':contactform})
@login_required
def todoadd(request):
    todoform=TodoForm(request.POST or None)
    if todoform.is_valid():
        todoform.save()
        return redirect("todolist")
    return render(request,"todoadd.html",{"forms":todoform})
@login_required
def todolist(request):
    allfeedback=Todo.objects.all()
    return render(request,"todolist.html",{"todos":allfeedback})
 
def todoedit(request,pk):
    todo = get_object_or_404(Todo,pk=pk)
    todoform=TodoForm(request.POST or None,instance=todo)
    if todoform.is_valid():
        todoform.save()
        return redirect ("todolist")
    return render(request,"todoadd.html",{"forms":todoform})

def tododelete(request,pk):
    todo = get_object_or_404(Todo,pk=pk)
    
    if request.method=="POST":
        todo.delete()
        return redirect ("todolist")
    return render(request,"tododelete.html",{"todo":todo})