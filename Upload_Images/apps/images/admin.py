from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):

    """ Add model Image to django admin panel """
    list_display = ['id', 'user', 'tier', 'title', 'date_creation']
    list_filter = ['user', 'date_creation']
    list_display_links = ['user', 'title', 'tier']


admin.site.register(Image, ImageAdmin)

