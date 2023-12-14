from django.forms import forms
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from user.models import User


# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'user/example.html')


def method(request: HttpRequest) -> HttpResponse:
    name = request.POST.get('name', 'undefined')
    email = request.POST.get('email', 'undefined')

    user = User.objects.create(name=name, email=email)
    user.save()

    return HttpResponse(f'Name: {name}; Email: {email}')
