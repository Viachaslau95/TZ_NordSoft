from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'phone', 'is_admin', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name',)
    list_display_links = ['email']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('email',)


admin.site.register(Account, AccountAdmin)

# try:
#     Account.objects.get_by_natural_key('admin')
# except Account.DoesNotExist:
#     Account.objects.create_superuser(
#         'test@mail.ru', 'fntest', 'lntest', '777', 'test')
