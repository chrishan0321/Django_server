from django.shortcuts import render
from django.http import JsonResponse
import json

def showmain(request):
    return render(request, "keyLog.html")

def posted(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get("user_id")
        key = data.get("key")
        keys = ''
        return JsonResponse({"status" : "success"})
