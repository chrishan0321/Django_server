from django.shortcuts import render
# def 함수이름(인자):
#   함수를 호출했을 때 실행될 코드
# Create your views here.
def showmain(request):
    return render(request, "main/mainpage.html")