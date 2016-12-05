from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render

from .models import Student


def index(request):
    if request.user.is_authenticated:
        slist = Student.objects.all()
        toppers = Student.objects.order_by('-cgpa')[:3]
        context = {'s_list': slist, 'toppers': toppers}
        return render(request, 'authdb/index.html', context)
    else:
        return render(request, 'authdb/invalidlogin.html')


def details(request, sid):
    if request.user.is_authenticated:
        std = get_object_or_404(Student, id=sid)
        context = {'std': std}
        return render(request, 'authdb/details.html', context)
    else:
        return render(request, 'authdb/invalidlogin.html')


def login_view(request):
    return render(request, 'authdb/login.html')


def login_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        slist = Student.objects.all()
        toppers = Student.objects.order_by('-cgpa')[:3]
        context = {'s_list': slist, 'toppers': toppers}
        return render(request, 'authdb/index.html', context)
    else:
        return render(request, 'authdb/invalidlogin.html')


def logout_view(request):
    logout(request)
    return render(request, 'authdb/logout.html')
