from django.shortcuts import render
from .models import Project
from django.views.generic import ListView

class ProjectListView(ListView):
    model = Project
    template_name = 'projects_tool/project_list.html'  # Update this to your template path
    context_object_name = 'projects'  # Name of the variable to access in the template

def homepage(request):
    return HttpResponse("Welcome to the Project Management Homepage!")
