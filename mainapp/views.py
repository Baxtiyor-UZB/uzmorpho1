from django.shortcuts import render
from .models import *
from django.db.models import Q 
# Create your views here.
def index(request):

    return render(request,"index.html")
def ishchi(request):
    
    return render(request,"ishchi.html")
word1="salom"
def stemming(request):
    word1=str(request.GET.get('word1'))
    
    try:
        if word1:

            word1 = wfroottab.objects.filter(wf=word1)
            
        
    except :
        a=1    
    return render(request,"stemming.html",{'word1':word1})
def lematizatsiya(request):
    word2=str(request.GET)
    return render(request,"lematizatsiya.html",{'word2':word2})
def morfemik_tahlil(request):
    word3=str(request.GET)
    return render(request,"morfemik_tahlil.html",{'word3':word3})
def asosdosh_sozlar(request):
    word4=str(request.GET.get('word4'))
    try:
        if word4:
            word4 = wfroottab.objects.filter(Q(wf__icontains=word4))      
        else:
            word4 = wfroottab.objects.all().order_by("-date_created")
    except :
        a=1    
    return render(request,"asosdosh_sozlar.html",{'word4':word4})