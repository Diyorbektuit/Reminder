from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True


class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='telegram')

    def __str__(self):
        return self.username or str(self.telegram_id)
