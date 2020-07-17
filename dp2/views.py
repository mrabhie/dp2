from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello world")
def home(request):
    return HttpResponse("<h1> welcome to  homepage <h1>")
def htmld(request):
    return render(request,"sample1.html")
