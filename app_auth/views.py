from django.shortcuts import render, redirect, HttpResponse

# auth组件
from django.contrib import auth
from django.contrib.auth.models import User

# forms组件
from app_auth.auth_forms import UserForm, UserFormLogin

import json


def reg(request):
    """ 注册 """
    # post
    if request.method == "POST":
        usr = request.POST.get('usr')
        pwd = request.POST.get('pwd')
        r_pwd = request.POST.get('r_pwd')
        form = UserForm(request.POST)
        # forms规则校验
        if form.is_valid():
            User.objects.create_user(username=usr, password=pwd)
            # 注册成功提示
            return redirect('/app_auth/reg_success/')
        else:
            # 继续注册
            return render(request, 'auth/reg.html', locals())
    # get
    form = UserForm()
    return render(request, "auth/reg.html", locals())


def reg_success(request):
    """ 注册成功提示 """
    return render(request, "auth/reg_success.html")


def login(request):
    """ 登录 """
    # post
    if request.method == "POST":
        usr = request.POST.get('usr')
        pwd = request.POST.get('pwd')
        form = UserFormLogin(request.POST)
        # 自定义认证状态
        res = {'usr': None, 'msg': None}
        # forms规则校验
        if form.is_valid():
            obj = auth.authenticate(username=usr, password=pwd)
            # auth认证校验
            if obj:
                auth.login(request, obj)
                res['usr'] = obj.username
            else:
                res['msg'] = '账号或密码错误'
        else:
            res['msg'] = '账号或密码不能为空'
        # 返回认证状态 --> login.js -> ajax
        res = json.dumps(res)
        return HttpResponse(res)
    # get
    form = UserFormLogin()
    return render(request, "auth/login.html", locals())


def logout(request):
    """ 登出 """
    auth.logout(request)
    return redirect('/app_auth/login/')
