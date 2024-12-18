from django import forms
from .models import Reminder

class ReminderPostForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'text', 'date']


class ReminderPatchForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'text', 'date', 'status']


class ReminderGetForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'text', 'date', 'status']
