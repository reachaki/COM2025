from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Project, Board, List, Task, Label

# Create resource classes for each model
class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project

class BoardResource(resources.ModelResource):
    class Meta:
        model = Board

class ListResource(resources.ModelResource):
    class Meta:
        model = List

class TaskResource(resources.ModelResource):
    class Meta:
        model = Task

class LabelResource(resources.ModelResource):
    class Meta:
        model = Label

# Customizing the admin interface with import/export functionality
@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResource
    list_display = ('title', 'slug', 'description')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Board)
class BoardAdmin(ImportExportModelAdmin):
    resource_class = BoardResource
    list_display = ('title', 'project')
    search_fields = ('title',)

@admin.register(List)
class ListAdmin(ImportExportModelAdmin):
    resource_class = ListResource
    list_display = ('title', 'board', 'position')
    search_fields = ('title',)
    list_filter = ('board',)

@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):
    resource_class = TaskResource
    list_display = ('title', 'list', 'priority', 'story_points')
    search_fields = ('title',)
    list_filter = ('priority', 'list')
    ordering = ('-story_points',)

@admin.register(Label)
class LabelAdmin(ImportExportModelAdmin):
    resource_class = LabelResource
    list_display = ('title', 'project', 'color')
    search_fields = ('title',)
    list_filter = ('project',)
