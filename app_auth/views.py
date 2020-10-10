from django.shortcuts import render, redirect, HttpResponse

# auth组件
from django.contrib import auth
from django.contrib.auth.models import User

# forms组件
from app_auth.auth_forms import UserForm, UserFormLogin

import json


def reg(request):
    if request.method == "POST":
        usr = request.POST.get('usr')
        pwd = request.POST.get('pwd')
        r_pwd = request.POST.get('r_pwd')
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            User.objects.create_user(username=usr, password=pwd)
            return redirect('/login/')
        else:
            print(form.cleaned_data)
            print(form.errors)
            print(type(form.errors))
            return render(request, 'reg.html', locals())
    form = UserForm()
    return render(request, "reg.html", locals())


def login(request):
    form = UserFormLogin()
    return render(request, "login.html", locals())


def login_auth(request):
    usr = request.POST.get('usr')
    pwd = request.POST.get('pwd')
    form = UserFormLogin(request.POST)
    res = {'usr': None, 'msg': None}
    if form.is_valid():
        obj = auth.authenticate(username=usr, password=pwd)
        if obj:
            auth.login(request, obj)
            res['usr'] = obj.username
        else:
            res['msg'] = '账号或密码错误'
    res = json.dumps(res)
    return HttpResponse(res)


def home(request):
    if request.user.is_anonymous:
        return redirect('/login/')
    return render(request, "home.html")


def logout(request):
    auth.logout(request)
    return redirect('/login')
