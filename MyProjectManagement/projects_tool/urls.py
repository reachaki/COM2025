from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import ProjectListView, ProjectViewSet, BoardViewSet, ListViewSet, TaskViewSet, LabelViewSet

# Create a router for the main API
router = DefaultRouter()
router.register(r'projects', ProjectViewSet)  # Register main projects API

# Create a nested router for boards, lists, tasks, and labels
projects_router = routers.NestedDefaultRouter(router, r'projects', lookup='project')
projects_router.register('boards', BoardViewSet, basename='project-boards')
projects_router.register('lists', ListViewSet, basename='project-lists')
projects_router.register('tasks', TaskViewSet, basename='project-tasks')
projects_router.register('labels', LabelViewSet, basename='project-labels')

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),  # This could render a project list view
    path('api/', include(router.urls)),  # Include main API routes
    path('api/projects/', include(projects_router.urls)),  # Include nested API routes specifically for projects
]
