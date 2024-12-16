from django.test import TestCase
from django.contrib.auth.models import User
from .models import Reminder
from datetime import datetime

class ReminderModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")

    def test_create_reminder(self):
        reminder = Reminder.objects.create(
            title="Test Reminder",
            text="This is a test reminder",
            date=datetime.now(),
            user=self.user,
            status="pending"
        )
        self.assertEqual(reminder.title, "Test Reminder")
        self.assertEqual(reminder.status, "pending")
        self.assertEqual(reminder.user, self.user)
