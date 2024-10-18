from django.shortcuts import render
from django.http import HttpResponse  # Ensure to import HttpResponse
from .models import Project, Board, List, Task, Label
from django.views.generic import ListView
from rest_framework import viewsets
from .serializers import ProjectSerializer, BoardSerializer, ListSerializer, TaskSerializer, LabelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ProjectListView(ListView):
    model = Project
    template_name = 'projects_tool/project_list.html'  # Update this to your template path
    context_object_name = 'projects'  # Name of the variable to access in the template

def homepage(request):
    return HttpResponse("Welcome to the Project Management Homepage!")

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class YourAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})


class ProjectsAPIView(APIView):
    def get(self, request):
        # Logic to retrieve project data (e.g., from the database)
        return Response({"projects": "List of projects"})


