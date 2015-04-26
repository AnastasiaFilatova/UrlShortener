from django.conf import settings
from django.shortcuts import render, redirect
from shortener import forms
from models import Url, Word
from urlparse import urlparse
from utils import shortificator
import time

def handle_form(request):
    start = int(round(time.time()*1000))
    if request.method == 'POST':
        form = forms.UrlForm(request.POST)
        if form.is_valid():
            url_path = urlparse(form.cleaned_data['base_url']).path
            all_words = [word.word for word in list(Word.objects.all())]
            used_words = [{'key': url.key, 'date': url.date} for url in list(Url.objects.all())]
            key = shortificator(url_path, all_words, used_words)
            new_url = Url(key=key, base_url=form.cleaned_data['base_url'],
                          short_url="{}{}/".format(settings.SITE_URL, key))
            new_url.save()
            answer = dict()
            answer['old'] = form.cleaned_data['base_url']
            answer['new'] = new_url.short_url
            answer['time'] = (float(round(time.time()*1000)) - start)/1000
            return render(request, 'answer.html', {'url': answer})
        else:
            return render(request, 'form.html', {'form': form })
    else:
        return render(request, 'form.html', {'form': forms.UrlForm() })

def redirect_url(request):
    key = request.path.strip('/')
    url = Url.objects.get(key=key)
    if url:
        return redirect(url.base_url)
    return render(request, '404.html')