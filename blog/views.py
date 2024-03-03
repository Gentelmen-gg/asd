from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html')


def adress(request):
    return render(request, 'blog/factory.html')

def categ(request):
    return render(request, 'blog/cate.html')

def qwert(request):
    return render(request, 'blog/qwert.html')