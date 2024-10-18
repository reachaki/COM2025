from django.core.management.base import BaseCommand
from projects_tool.models import Project

class Command(BaseCommand):
    help = 'Seeds the database with sample data for projects'

    def handle(self, *args, **kwargs):
        # Define sample projects
        projects_data = [
            {"title": "Project 1", "description": "This is the first sample project."},
            {"title": "Project 2", "description": "This is the second sample project."},
            {"title": "Project 3", "description": "This is the third sample project."},
            {"title": "Project 4", "description": "This is the fourth sample project."},
            {"title": "Project 5", "description": "This is the fifth sample project."},
            {"title": "Project 6", "description": "This is the sixth sample project."},
            {"title": "Project 7", "description": "This is the seventh sample project."},
            {"title": "Project 8", "description": "This is the eighth sample project."},
            {"title": "Project 9", "description": "This is the ninth sample project."},
            {"title": "Project 10", "description": "This is the tenth sample project."},
        ]

        # Create projects
        for project_data in projects_data:
            project = Project(**project_data)
            project.save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with sample projects.'))
