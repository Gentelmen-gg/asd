from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse

def index(request):
    return render(request, 'blog/index.html')


def adress(request):
    return render(request, 'blog/factory.html')

def categ(request, catid):
    return HttpResponse(f'<h1>Page {catid}</h1>')



def qwert(request):
    return render(request, 'blog/qwert.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1 style="text-align:center">Неее братан, нет такой страницы</h1>')