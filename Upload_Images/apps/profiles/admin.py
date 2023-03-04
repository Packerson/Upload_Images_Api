from django.contrib import admin
from .models import Profile, Custom


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'tier']
    list_filter = ['tier']
    list_display_links = ['id', 'user']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Custom)
