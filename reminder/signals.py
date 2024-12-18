from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, ClockedSchedule
import json
from .models import Reminder


@receiver(post_save, sender=Reminder)
def create_periodic_task(sender, instance, created, **kwargs):
    if created:
        clocked_schedule, _ = ClockedSchedule.objects.get_or_create(
            clocked_time=instance.date
        )

        task_kwargs = {'reminder_id': instance.id}

        task, created = PeriodicTask.objects.get_or_create(
            name=f"Send Reminder {instance.id}",
            defaults={
                "task": "reminder.tasks.send_reminder_task",
                "clocked": clocked_schedule,
                "enabled": True,
                "kwargs": json.dumps(task_kwargs),
                "one_off": True,
            },
        )

        if not created:
            task.clocked = clocked_schedule
            task.kwargs = json.dumps(task_kwargs)
            task.enabled = True
            task.save()

