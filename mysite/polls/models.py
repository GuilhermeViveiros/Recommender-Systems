from django.db import models

# Create your models here.

from django.db import models

class User_id(models.Model):
    user_name = models.CharField(max_length=30)
    user_id = models.IntegerField()