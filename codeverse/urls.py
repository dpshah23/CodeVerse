from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')), 
    path('',include('error_handling.urls')),
    path('auth/', include('auth1.urls')),
    path('dj-admin/', admin.site.urls),
    
]
