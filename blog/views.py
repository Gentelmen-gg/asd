from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponse, Http404

def index(request):
    return render(request, 'blog/index.html')


def adress(request):
    return render(request, 'blog/factory.html')

def categ(request, catid):
    if request.GET:
        print('Имя:', request.GET['name'])
        print('Возраст:', request.GET['age'])
    if int(catid) == 50:
        raise Http404
    if int(catid) == 1000:
        return redirect('home')
    if int(catid) == 500:
        return redirect('second', pernament=True)
    else:
        print('Нет данных!')
    return HttpResponse(f'<h1>Page {catid}</h1>')



def qwert(request):
    return render(request, 'blog/qwert.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Неее братан, нет такой страницы</h1>')