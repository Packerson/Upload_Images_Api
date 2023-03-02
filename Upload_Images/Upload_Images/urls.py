from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('djoser.urls')),
    path('api-auth/', include('djoser.urls.jwt')),
    path('api-auth/profile/', include("apps.profiles.url"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""header= show on logging screen
    title = 
    index_title = """
admin.site.site_header = "Upload Images Admin Panel"
admin.site.site_title = "Upload Images Admin Site"
admin.site.index_title = "Welcome to the Upload Images Site"
