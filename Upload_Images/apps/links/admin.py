from django.contrib import admin
from .models import Links


class LinksAdmin(admin.ModelAdmin):

    list_display = ['id', 'user', 'time', 'date_creation', 'expiration_date']
    list_filter = ['user', 'time', 'date_creation']
    list_display_links = ['user', 'time', 'date_creation']


admin.site.register(Links, LinksAdmin)
