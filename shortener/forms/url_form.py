from django import forms

class SubmittForm(forms.Form):
    url_to_submitt = forms.URLField()


