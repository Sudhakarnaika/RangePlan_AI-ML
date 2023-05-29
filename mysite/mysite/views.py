
from django.shortcuts import render
from django.http import HttpResponse

def analyze(request):

    params= {'purpose':'Remove functuations', 'analyzed_text':'analyzed'}
    return render(request,'analyze.html', params)
