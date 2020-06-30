from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *

#Create your views here.

def user_exist(request):
    context = {
        'pageTitle':'REGISTER',
    }
    return render(request, 'main/user_exist.html', context)

def wrong_token(request):
    context = {
        'pageTitle':'REGISTER',
    }
    return render(request, 'main/wrong_token.html', context)

def null_hak_pilih(request, uuid):
    user = User.objects.get(uuid=uuid)
    context = {
        'user':user,
        'pageTitle':'PILIH',
    }
    return render(request, 'main/null_hak_pilih.html', context)

def register_form(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            token = form.cleaned_data.get('token')

            a = Calon.objects.all()

            for i in a:
                if username == i.username or email == i.email:
                    return user_exist(request)

            if token != "12345":
                return wrong_token(request)

            new_user = Calon(username=username, email=email, password=password)
            new_user.save()
            return redirect('/')
    else:
        form = RegisterForm()
    
    context = {
        'form':form,
    }

    return render(request, 'main/register.html', context)

def loginView(request):
    form = LoginForm()
    condition = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user:
                condition = False
                login(request, user)
                return redirect('/accounts/dashboard/'+str(user.uuid))
            else:
                condition = True
    else:
        form = LoginForm()

    context = {
        'form':form,
        'pageTitle':'LOGIN',
        'condition':condition,
    }

    return render(request, 'main/login.html', context)


def logoutView(request):
    logout(request)
    return redirect('/accounts/logout')

@login_required
def dashboardView(request, uuid):
    user = User.objects.get(uuid=uuid)
    list_calon = Calon.objects.all()
    context = {
        'user':user,
        'calon':list_calon,
    }
    return render(request, 'main/dashboard.html', context)