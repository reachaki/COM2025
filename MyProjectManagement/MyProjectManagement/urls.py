from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects_tool.urls')),  # Include your app's URLs for web views
    path('api/', include('MyProjectManagement.api_urls')),  # Include your app's URLs for all APIs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
