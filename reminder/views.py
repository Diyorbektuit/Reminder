from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import ReminderPostForm, ReminderPatchForm


def reminder_list(request):
    status_filter = request.GET.get('status')
    user = request.user
    if user.is_anonymous():
        return redirect('login')

    if status_filter == 'done':
        reminders = user.reminders.filter(status=True).order_by('-date')
    elif status_filter == 'not_done':
        reminders = user.reminders.filter(status=False).order_by('-date')
    else:
        reminders = user.reminders.all().order_by('-date')

    paginator = Paginator(reminders, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'reminder_list.html', {
        'page_obj': page_obj,
        'status_filter': status_filter
    })


def reminder_create(request):
    user = request.user
    if user.is_anonymous():
        return redirect('login')
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


def reminder_mark_done(request, pk):
    user = request.user
    if user.is_anonymous():
        return redirect('login')
    reminder = user.reminders.filter(id=pk)
    if not reminder.exists():
        return render(request, '404.html')
    reminder = reminder.first()
    reminder.status = True
    reminder.save()
    return redirect('reminder_list')


def reminder_update(request, pk):
    user = request.user
    if user.is_anonymous():
        return redirect('login')
    reminder = user.reminders.filter(id=pk)
    if not reminder.exists():
        return render(request, '404.html')
    reminder = reminder.first()
    if request.method == 'POST':
        form = ReminderPatchForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('reminder_list')
    else:
        form = ReminderPatchForm(instance=reminder)
    return render(request, 'reminder_form.html', {'form': form})


def reminder_delete(request, pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    reminder = user.reminders.filter(id=pk)
    if not reminder.exists():
        return render(request, '404.html')
    reminder = reminder.first()
    if request.method == 'POST':
        reminder.delete()
        return redirect('reminder_list')
    return render(request, 'reminder_confirm_delete.html', {'reminder': reminder})
