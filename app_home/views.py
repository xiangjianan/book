from django.shortcuts import render, redirect

# auth组件
from django.contrib import auth
from django.contrib.auth.models import User

# forms组件
from app_home.home_forms import *
from app_home.models import *
import json


# Create your views here.

def home(request):
    if request.user.is_anonymous:
        return redirect('/app_auth/login/')
    else:
        usr = request.user.username
        return render(request, "home/home.html", locals())


def publish(request):
    usr = request.user.username
    return render(request, "home/publish.html", locals())


def author(request):
    usr = request.user.username
    return render(request, "home/author.html", locals())


def add_book(request):
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        pub_id = request.POST.get('pub_id')
        auth_id_list = request.POST.getlist('auth_id_list')
        form = AddFormBook(request.POST)
        # forms校验通过
        if form.is_valid():
            book_obj = Book.objects.create(book_name=book_name, pub_id=pub_id)
            book_obj.auth.add(*auth_id_list)
            # 重定向登录界面
            return redirect('/app_home/home/')
        else:
            # forms校验不通过，继续注册
            return render(request, 'auth/reg.html', locals())
    form = AddFormBook()
    pub_obj = Publish.objects.all()
    auth_obj = Author.objects.all()
    return render(request, "home/add_book.html", locals())


def add_auth(request):
    if request.method == "POST":
        auth_name = request.POST.get('auth_name')
        form = AddFormAuth(request.POST)
        # forms校验通过
        if form.is_valid():
            Author.objects.create(auth_name=auth_name)
            # 重定向登录界面
            return redirect('/app_home/home/')
        else:
            # forms校验不通过，继续注册
            return render(request, 'auth/reg.html', locals())
    form = AddFormAuth()
    return render(request, "home/add_auth.html", locals())


def add_pub(request):
    if request.method == "POST":
        pub_name = request.POST.get('pub_name')
        form = AddFormPub(request.POST)
        # forms校验通过
        if form.is_valid():
            Publish.objects.create(pub_name=pub_name)
            # 重定向登录界面
            return redirect('/app_home/home/')
        else:
            # forms校验不通过，继续注册
            return render(request, 'auth/reg.html', locals())
    form = AddFormPub()
    return render(request, "home/add_pub.html", locals())
