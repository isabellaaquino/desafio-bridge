from django.db import models

# Create your models here.
class Number(models.Model):
    n1 = models.IntegerField()
    n2 = models.IntegerField()
    primos = models.JSONField(default=[])

# Number.objects.create(n1='', n2='')