from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Project, Board, List, Task, Label
from import_export.fields import Field
from import_export.widgets import DateWidget 
import logging


logger = logging.getLogger(__name__)

# Create resource classes for each model
from import_export import fields, resources



class ProjectResource(resources.ModelResource):
    created_at = fields.Field(
        column_name='created_at',
        attribute='created_at',
        widget=DateWidget(format='%Y-%m-%d %H:%M')
    )

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'image', 'slug', 'created_at')

    def dehydrate_created_at(self, project):
        return project.created_at.strftime('%Y-%m-%d %H:%M') if project.created_at else ''

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
    list_display = ('title', 'slug', 'description', 'created_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
   

# The explicit registration line is removed
# admin.site.register(Project, ProjectAdmin)

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
