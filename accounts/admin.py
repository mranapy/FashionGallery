from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'last_login', 'is_admin','is_active','is_staff','is_superuser')
    readonly_fields = ('last_login','date_joined','is_superuser',)
    ordering = ['-date_joined']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)