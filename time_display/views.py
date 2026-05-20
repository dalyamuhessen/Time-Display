from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from time import gmtime,strftime
def index(request):
    context={
           "time":datetime.now().strftime("%B %d , %Y - %I:%M %p")
            #  "time": strftime("%Y-%m-%d %H:%M %p", gmtime()) 
            # "time":datetime.now().strftime("%B %d , %Y - %I:%M %p")
    }        
    return render(request, 'index.html', context)
