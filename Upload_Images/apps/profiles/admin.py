from django.contrib import admin, messages
from .models import Profile, Custom


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'tier']
    list_filter = ['tier']
    list_display_links = ['id', 'user']

    def save_model(self, request, obj, form, change):

        messages.add_message(request, messages.INFO,
                             'If you want to choose custom resolution, '
                             'need to choose Tier= CUSTOM.'
                             'Otherwise custom resolution will be set to none'
                             )
        super(ProfileAdmin, self).save_model(request, obj, form, change)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Custom)
