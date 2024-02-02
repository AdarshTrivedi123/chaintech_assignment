from django.db import models
from datetime import datetime
# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    category=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)