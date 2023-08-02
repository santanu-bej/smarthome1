from django.db import models


class Switch(models.Model):
    id = models.AutoField(primary_key=True)
    switch_name = models.CharField(max_length=100,unique=True)
    switch_status = models.BooleanField(default=False)