from django.contrib import admin
from .models import Links


class LinksAdmin(admin.ModelAdmin):

    list_display = ['id','image', 'time', 'date_creation', 'expiration_date', 'expiration_link']
    list_filter = ['time', 'date_creation']
    list_display_links = ['time', 'date_creation']


admin.site.register(Links, LinksAdmin)
