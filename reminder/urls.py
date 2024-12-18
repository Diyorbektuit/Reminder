from django.urls import path
from . import views

urlpatterns = [
    path('reminders/', views.reminder_list, name='reminder_list'),
    path('reminders/create/', views.reminder_create, name='reminder_create'),
    path('reminders/<int:pk>/update/', views.reminder_update, name='reminder_update'),
    path('reminders/<int:pk>/delete/', views.reminder_delete, name='reminder_delete'),
    path('reminder/<int:pk>/mark_done/', views.reminder_mark_done, name='reminder_mark_done'),
]
