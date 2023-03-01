from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','is_basic', 'is_premium', "is_enterprise"]
    list_filter = ['is_basic', 'is_premium', "is_enterprise"]
    list_display_links = ['id', 'user']


admin.site.register(Profile, ProfileAdmin)
