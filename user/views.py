from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'user/example.html')


def method(request: HttpRequest) -> HttpResponse:
    name = request.POST.get('name', 'undefined')
    email = request.POST.get('email', 'undefined')
    return HttpResponse(f'Name: {name}; Email: {email}')
