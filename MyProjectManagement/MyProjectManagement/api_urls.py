from django.urls import path
from projects_tool.views import YourAPIView, ProjectsAPIView  # Replace with your actual view classes

urlpatterns = [
    path('example/', YourAPIView.as_view(), name='example_view'),  # Existing endpoint
    path('projects/', ProjectsAPIView.as_view(), name='projects_view'),  # New projects endpoint
]
