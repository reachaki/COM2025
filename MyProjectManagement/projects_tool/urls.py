from django.urls import path
from .views import ProjectListView  # Import your class-based view

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),  # Set the path for the project list view
]
