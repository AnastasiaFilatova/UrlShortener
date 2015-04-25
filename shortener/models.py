from django.conf import settings
from django.db import models
from views import get_word

class Url(models.Model):
    """
    A base url
    """
    base_url = models.URLField()

    def short_url(self):
        return settings.SITE_URL + self.get_word()

    def __unicode__(self):
        return self.base_url

class Word(models.Model):
    word = models.CharField(max_length=255)

    def __unicode__(self):
        return self.word