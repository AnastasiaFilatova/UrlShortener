from django import forms

class UrlForm(forms.Form):
    base_url = forms.URLField()

    """def cleaned_data(self):
        base_url = self.cleaned_data['base_url']
        return base_url"""