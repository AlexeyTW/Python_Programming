from django.db import models
from django.conf import settings


class Feedback(models.Model):
    text = models.CharField(verbose_name='User feedback', max_length=5000)
    grade = models.IntegerField(verbose_name='Assessment')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(verbose_name='Object', max_length=100)
