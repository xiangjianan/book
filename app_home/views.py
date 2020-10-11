from django.shortcuts import render, redirect


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
