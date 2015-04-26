from django.shortcuts import render
from shortener import forms
from models import Url, Word
from urlparse import urlparse
import re
import logging


logging.basicConfig(level=logging.DEBUG)

def get_base_url(request):
    logging.debug("get_base_url")
    if request.method == 'POST':
        form = forms.UrlForm(request.POST)
        if form.is_valid():
            url = dict()
            url['old'] = form.cleaned_data['base_url']
            url['new'] = shortificator(url['old'])
            url_model = Url(id=hashlib.sha1(url['old']).hexdigest(), base_url=url['old'], short_url=url['new'])
            url_model.save()
            logging.debug('base_url saved {}'.format(form.cleaned_data['base_url']))
            return render(request, 'answer.html', {'url': url})
        else:
            logging.debug('base_url was not saved')
            return render(request, 'form.html', {'form': form })
    else:
        return render(request, 'form.html', {'form': forms.UrlForm() })
