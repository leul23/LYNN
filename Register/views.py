from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib.auth import login, authenticate

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Home:index')
    else:
        form = UserRegistration()
    return render (request,'Register/index.html',{'form' : form})