from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

text = ["first","second","third"]

def index(request):
    return render(request,'myapp/index.html')

def send(request,num):
    return HttpResponse(text[num])
