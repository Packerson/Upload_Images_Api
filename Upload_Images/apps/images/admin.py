from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'date_creation']
    list_filter = ['user', 'date_creation', 'title']
    list_display_links = ['user', 'title']


# admin.site.register(Image)
admin.site.register(Image, ImageAdmin)

