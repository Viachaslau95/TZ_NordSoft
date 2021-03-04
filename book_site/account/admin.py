from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_admin', 'is_active')
    search_fields = ('email', 'first_name', 'last_name',)
    list_display_links = ['email']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('email',)


admin.site.register(Account, AccountAdmin)

