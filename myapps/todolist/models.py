from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class TodoItem(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="todoitem")

    def __str__(self):
        return self.name