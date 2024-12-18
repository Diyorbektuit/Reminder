from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reminder
from django.core.paginator import Paginator
from .forms import ReminderPostForm, ReminderPatchForm


def reminder_list(request):
    status_filter = request.GET.get('status')
    user = request.user

    if status_filter == 'done':
        reminders = Reminder.objects.filter(status=True, user=user).order_by('-date')
    elif status_filter == 'not_done':
        reminders = Reminder.objects.filter(status=False, user=user).order_by('-date')
    else:
        reminders = Reminder.objects.filter(user=user).order_by('-date')

    paginator = Paginator(reminders, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'reminder_list.html', {
        'page_obj': page_obj,
        'status_filter': status_filter
    })


@login_required
def reminder_create(request):
    if request.method == 'POST':
        form = ReminderPostForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            return redirect('reminder_list')
    else:
        form = ReminderPostForm()
    return render(request, 'reminder_form.html', {'form': form})


@login_required()
def reminder_mark_done(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    reminder.status = True
    reminder.save()
    return redirect('reminder_list')


@login_required
def reminder_update(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReminderPatchForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('reminder_list')
    else:
        form = ReminderPatchForm(instance=reminder)
    return render(request, 'reminder_form.html', {'form': form})


@login_required
def reminder_delete(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk, user=request.user)
    if request.method == 'POST':
        reminder.delete()
        return redirect('reminder_list')
    return render(request, 'reminder_confirm_delete.html', {'reminder': reminder})
