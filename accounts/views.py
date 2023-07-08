from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login

# Create your views here.
def signup(request):
    signupfom=UserCreationForm(request.POST or None)
    if signupfom.is_valid():
        signupfom.save()
        username=signupfom.cleaned_data.get('username')
        raw_password=signupfom.cleaned_data.get('password1')
        user=authenticate(username=username,password=raw_password)
        login(request,user)
        return redirect("todolist")
    return render(request,'signup.html',{'form':signupfom})
