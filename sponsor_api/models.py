from django.db import models

class Keywords(models.Model):
    keyword = models.CharField(max_length=50)