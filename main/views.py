from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'title' : 'Home',
        'content': 'Glavvnay'
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('Result')