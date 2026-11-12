from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def salom(request):
    students = Students.objects.all()
    
    context = {
        "students": students
    }   
    return render(request, "salom.html", context)
    