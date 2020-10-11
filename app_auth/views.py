from django.shortcuts import render, redirect, HttpResponse

# auth组件
from django.contrib import auth
from django.contrib.auth.models import User

# forms组件
from app_auth.auth_forms import UserForm, UserFormLogin

import json


def reg(request):
    # 注册按钮提交
    if request.method == "POST":
        usr = request.POST.get('usr')
        pwd = request.POST.get('pwd')
        r_pwd = request.POST.get('r_pwd')
        form = UserForm(request.POST)
        # forms校验通过
        if form.is_valid():
            User.objects.create_user(username=usr, password=pwd)
            # 重定向登录界面
            return redirect('/login/')
        else:
            # forms校验不通过，继续注册
            return render(request, 'auth/reg.html', locals())
    # url请求
    form = UserForm()
    return render(request, "auth/reg.html", locals())


def login(request):
    # 登录按钮提交
    if request.method == "POST":
        usr = request.POST.get('usr')
        pwd = request.POST.get('pwd')
        form = UserFormLogin(request.POST)
        res = {'usr': None, 'msg': None}
        # forms校验通过
        if form.is_valid():
            obj = auth.authenticate(username=usr, password=pwd)
            # 用户认证通过
            if obj:
                auth.login(request, obj)
                res['usr'] = obj.username
            # 用户认证失败
            else:
                res['msg'] = '账号或密码错误'
        else:
            res['msg'] = '账号或密码不能为空'
        # 通过json返回认证状态
        res = json.dumps(res)
        return HttpResponse(res)
    # url请求
    form = UserFormLogin()
    return render(request, "auth/login.html", locals())


def home(request):
    if request.user.is_anonymous:
        return redirect('/login/')
    else:
        usr = request.user.username
        return render(request, "home/home.html", locals())


def logout(request):
    auth.logout(request)
    return redirect('/login')


def publish(request):
    usr = request.user.username
    return render(request, "home/publish.html", locals())


def author(request):
    usr = request.user.username
    return render(request, "home/author.html", locals())
