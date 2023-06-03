from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import signup_form,login_form
from django.contrib import messages
# Create your views here.


# def home(request):
#     if request.method == 'POST':
#         form = UF(request.POST)
#         if form.is_valid():
#             messages.error(request, 'Your form is submitted successfully!', extra_tags='signup')
#             form.save()
        
        
#     form = UF()
#     return render(request,'app1/home.html',{'form':form})

def about(request): 
    return render(request, 'app1/about.html')

def dashboard(request):
    return render(request, 'app1/dashboard.html')

def logout(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            do_logout(request)
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponse('<h1>404 page not found!</h1>')
    else:
        return HttpResponseRedirect('/login/')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = signup_form(request.POST)
            if fm.is_valid():
                user = fm.save()
                # group = Group.objects.get(name='simple_user')
                # user.groups.add(group)
                messages.error(request, 'Your Account has been Created!', extra_tags='signup')
                fm = signup_form()
                return render(request, 'app1/signup.html',{'form':fm})

            return render(request, 'app1/signup.html',{'form':fm})
        fm = signup_form()
        return render(request, 'app1/signup.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = login_form(request=request, data=request.POST)
            uname = request.POST['username']
            passw = request.POST['password']
            if fm.is_valid():
                usr = authenticate(username=uname,password=passw)
                if usr is not None:
                    do_login(request, usr)
                    return HttpResponseRedirect('/dashboard/')  

            messages.error(request, 'Incorrect username or password', extra_tags='login')
            return render(request, 'app1/login.html',{'form':fm})        
        fm = login_form()
        return render(request, 'app1/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')