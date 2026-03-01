from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HTTP response
    return HttpResponse('Olá, Mundo! Meu site com Django!')

# HTTP REQUEST
def contato(request):
    # return HTTP response
    return HttpResponse('CONTATO')

# HTTP REQUEST
def sobre(request):
    # return HTTP response
    return HttpResponse('SOBRE')