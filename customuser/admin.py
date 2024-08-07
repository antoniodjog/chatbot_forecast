
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_admin')
    search_fields = ('username', 'email')
    readonly_fields = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, UserAdmin)
