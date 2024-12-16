from django.contrib import admin
from  .models import Reminder

# Register your models here.
def mark_as_active(modeladmin, request, queryset):
    queryset.update(status=True)
    modeladmin.message_user(request, "Tanlangan eslatmalar faollashtirildi.")

mark_as_active.short_description = "Tanlangan eslatmalarni faollashtirish"

# Custom admin klass
@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'status')
    list_filter = ('status', 'date')
    actions = [mark_as_active]
