from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, "hello/index.html")

def sy(request):
  return HttpResponse("Hello Sy_!")

def zst(request):
  return HttpResponse("Hello SiTuo!")

def greet(request, name):
  # return HttpResponse(f"Hello {name.capitalize()}") # 首字母大写
  return render(request, "hello/greet.html", {
    "name": name.capitalize()
  })