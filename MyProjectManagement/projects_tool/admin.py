from django.contrib import admin
from .models import Project, Board, List, Task, Label

# Customizing the Project admin interface
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')  # Display these fields in the list view
    search_fields = ('title',)  # Search by title field
    prepopulated_fields = {'slug': ('title',)}  # Auto-populate slug from title

# Customizing the Board admin interface
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'project')  # Display these fields
    search_fields = ('title',)  # Search by board title

# Customizing the List admin interface
class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'board', 'position')  # Display these fields
    search_fields = ('title',)  # Search by list title
    list_filter = ('board',)  # Add filter by board in the sidebar

# Customizing the Task admin interface
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'list', 'priority', 'story_points')  # Display these fields
    search_fields = ('title',)  # Search by task title
    list_filter = ('priority', 'list')  # Add filter by priority and list
    ordering = ('-story_points',)  # Order by story points, descending

# Customizing the Label admin interface
class LabelAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'color')  # Display these fields
    search_fields = ('title',)  # Search by label title
    list_filter = ('project',)  # Add filter by project in the sidebar

# Registering models and their admin customizations
admin.site.register(Project, ProjectAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Label, LabelAdmin)
