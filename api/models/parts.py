from django.db import models

class Part(models.Model):
    name = models.CharField(max_length=200)
    onHand = models.BigIntegerField(null=True ,blank=True)
    tool = models.CharField(max_length=200, blank=True)
