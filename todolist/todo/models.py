from typing import Text
from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text
        