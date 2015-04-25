from django.conf import settings
from django.db import models

class Url(models.Model):
    """
    A base url
    """
    base_url = models.URLField()

    def get_word(self):
        return 'Hello'

    def short_url(self):
        return settings.SITE_URL + self.get_word()

    def __unicode__(self):
        return self.base_url

class Word(models.Model):
    word = models.CharField(max_length=255)

    def __unicode__(self):
        return self.word