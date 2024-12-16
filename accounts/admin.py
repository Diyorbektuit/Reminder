from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import TelegramUser

# Register your models here.
admin.site.unregister(Group)
admin.site.unregister(User)


class TelegramUserInline(admin.StackedInline):
    model = TelegramUser
    can_delete = False
    verbose_name = "Telegram Foydalanuvchi"
    verbose_name_plural = "Telegram Foydalanuvchilar"


@admin.register(User)
class CustomUserAdmin(DefaultUserAdmin):
    inlines = (TelegramUserInline, )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ("Foydalanuvchi ma'lumotlari", {'fields': ('first_name', 'last_name')}),
        ('sanalar', {'fields': ('last_login', 'date_joined')}),
        ('ruhsatlar', {'fields': ('is_superuser', 'is_active', 'is_staff')})
    )

    list_filter = ('is_superuser', )
    readonly_fields = ('get_telegram_user', )
    filter_horizontal = ()

    def get_telegram_user(self, obj):
        return obj.telegram.id if obj.telegram else "-"

    get_telegram_user.short_description = "Telegram"


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'username', 'get_user')
    search_fields = ('telegram_id', 'username', 'user__username')

    def get_user(self, obj):
        return obj.user.username if obj.user else "-"
    get_user.short_description = "Foydalanuvchi"