from django.db import models
from django.contrib.auth.models import User
from accounts.models import BaseModel

class Reminder(BaseModel):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reminders')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
