from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser, DateTimeModel


class CustomUserAdmin(UserAdmin):

    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


class DateTimeModelAdmin(admin.ModelAdmin):

    list_display = ('formatted_datetime',)

    def formatted_datetime(self, obj):

        return obj.datetime

    formatted_datetime.short_description = 'DateTime'


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(DateTimeModel, DateTimeModelAdmin)

