from django.contrib import admin
from django.urls import path
from requests_testing.views import hello_world as requests_testing_entry  # Import and alias the hello_world view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Default home page
    path('my-page/', requests_testing_entry, name='hello_world'),  # URL for hello_world view
]

