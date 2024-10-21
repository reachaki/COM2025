from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Board, List, Task, Label
from django.views.generic import ListView
from rest_framework import viewsets
from .serializers import ProjectSerializer, BoardSerializer, ListSerializer, TaskSerializer, LabelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ProjectListView(ListView):
    model = Project
    template_name = 'projects_tool/project_list.html'
    context_object_name = 'projects'

def homepage(request):
    return HttpResponse("Welcome to the Project Management Homepage!")

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Board.objects.filter(project_id=project_id)

class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer

    def get_queryset(self):
        board_id = self.kwargs['board_id']
        return List.objects.filter(board_id=board_id)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        list_id = self.kwargs['list_id']
        return Task.objects.filter(list_id=list_id)

class LabelViewSet(viewsets.ModelViewSet):
    serializer_class = LabelSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Label.objects.filter(project_id=project_id)
