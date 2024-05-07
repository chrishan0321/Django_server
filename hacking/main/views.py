from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# def 함수이름(인자):
#   함수를 호출했을 때 실행될 코드
# Create your views here.
def showmain(request):
    return render(request, "mainpage.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        User.objects.create(username=username, pwd=pwd)
        return HttpResponse(f"welcome! {username}")
    return

def getUserData(request):
    queryset = User.objects.all()
    print(queryset)