from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Congragulations to one and all")
