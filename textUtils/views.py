# i have created this file- vishal
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello")
    return render(request,'index.html')

def analyze(request):
    dtext =request.GET.get('text', 'default')
    removepunc =request.GET.get('removepunc', 'off')
    print(removepunc)
    print(dtext)
    punctuations = ''',,..;/',..[[]]'''
    analyzed = ""
    for char in dtext:
        if char not in punctuations:
            analyzed=analyzed + char



    x= {'purpose':'remove punctuations', 'analyzed_text': analyzed }

    return render(request, 'analyze.html',x)
    
