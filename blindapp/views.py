from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, welcome to blindin. You're welcome to ask for referrals!")
