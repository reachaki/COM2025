from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectViewSet,
    BoardViewSet,
    ListViewSet,
    TaskViewSet,
    LabelViewSet,
    homepage,
    ProjectListView,
)

# Create a router and register the viewsets with it
router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'boards', BoardViewSet, basename='board')

urlpatterns = [
    path('api/', include(router.urls)),  # Include the router for API endpoints
    path('', homepage, name='homepage'),  # Home page route
    path('projects/', ProjectListView.as_view(), name='project_list'),  # Project list view
    
    # Nested routes for boards within projects
    path('api/projects/<int:project_id>/boards/', BoardViewSet.as_view({'get': 'list', 'post': 'create'}), name='project-boards'),
    path('api/projects/<int:project_id>/boards/<int:pk>/', BoardViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='project-board-detail'),

    # Nested routes for lists within boards
    path('api/projects/<int:project_id>/boards/<int:board_id>/lists/', ListViewSet.as_view({'get': 'list', 'post': 'create'}), name='board-lists'),
    path('api/projects/<int:project_id>/boards/<int:board_id>/lists/<int:pk>/', ListViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='board-list-detail'),

    # Nested routes for tasks within lists
    path('api/projects/<int:project_id>/boards/<int:board_id>/lists/<int:list_id>/tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='list-tasks'),
    path('api/projects/<int:project_id>/boards/<int:board_id>/lists/<int:list_id>/tasks/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='list-task-detail'),

    # Routes for labels
    path('api/projects/<int:project_id>/labels/', LabelViewSet.as_view({'get': 'list', 'post': 'create'}), name='project-labels'),
    path('api/projects/<int:project_id>/labels/<int:pk>/', LabelViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='project-label-detail'),
]
