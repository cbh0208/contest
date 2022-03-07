from django.conf.urls import url
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return render(request,'index.html')