# from django.http import HttpResponse
from django.shortcuts import render
from . models import place,team

# Create your views here.

def care(request):
    obj=place.objects.all()
    pro=team.objects.all()
    return render(request,'index.html',{'res':obj,'case':pro})
