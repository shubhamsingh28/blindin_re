from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, blindin_referral. You're are welcome to ask for referrals!")
