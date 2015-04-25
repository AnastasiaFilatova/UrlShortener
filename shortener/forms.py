from django import forms

class UrlForm(forms.Form):
    base_url = forms.URLField()

