from email.policy import default
from django.db import models

class Todo(models.Model):
    content = models.CharField(max_length = 255)
    isDone = models.BooleanField(default = False)

# Create your models here.
