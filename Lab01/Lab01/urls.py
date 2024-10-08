from django.contrib import admin
from django.urls import path
from requests_testing.views import hello_world as requests_testing_entry  # Import the hello_world view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my-page/', requests_testing_entry),  # Add this line
]
