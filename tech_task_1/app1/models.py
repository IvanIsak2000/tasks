from django.db import models


class Text(models.Model):
    id = models.CharField(primary_key=True)
    text = models.TextField()
    public = models.BooleanField()

