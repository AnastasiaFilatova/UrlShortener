from django.db import models

class Url(models.Model):
    base_url = models.URLField()
    short_url = models.URLField()
    key = models.CharField(max_length=100, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.base_url

class Word(models.Model):
    word = models.CharField(max_length=255)

    def __unicode__(self):
        return self.word