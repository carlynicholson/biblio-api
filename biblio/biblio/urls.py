from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authentication.urls')),
    path('api/', include('apps.api.urls')),
]
