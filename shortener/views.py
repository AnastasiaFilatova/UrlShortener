from django.shortcuts import render
from .models import Url, Word



def startpage(request):
    return render(request, 'startpage.html')








