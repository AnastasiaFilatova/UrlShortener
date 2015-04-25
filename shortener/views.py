from django.shortcuts import render
from shortener import forms


def startpage(request):
    return render(request, 'form.html')

def get_base_url(request):
    if request.method == 'POST':
        form = forms.UrlForm(base_url= request.POST)
        if form.is_valid():
            base_url = form.base_url
            return base_url
        else:
            form = forms.UrlForm()
            return render(request, 'form.html', {'form': form})

def get_word():
    pass





