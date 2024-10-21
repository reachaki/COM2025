# projects_tool/wizard.py
import data_wizard
from .models import Project, Board, List, Task  # Import your models

# Register your models with the data wizard
data_wizard.register(Project)
data_wizard.register(Board)
data_wizard.register(List)
data_wizard.register(Task)

# Sample data function to import data
def sample_data():
    print("Starting sample data import...") #troubleshoot
    # Sample data for projects
    projects_data = [
        {"title": "Sample Project with Cat Image", "description": "A project that includes an image.", "image": "project_images/cat_image.jpg"},
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

    # Create and save Project instances
    for project_data in projects_data:
        try:
            project, created = Project.objects.get_or_create(
                title=project_data['title'], 
                defaults={
                    "description": project_data.get("description", ""),
                    "image": project_data.get("image", None),
                }
            )
            if created:
                print(f"Created Project: {project.title}")
            else:
                print(f"Project already exists: {project.title}")
        except Exception as e:
            print(f"Error creating project {project_data['title']}: {e}")


    # Sample data for boards
    print("Completed project creation.")
    boards_data = [
        {"title": "Board 1", "project": Project.objects.get(title="Sample Project with Cat Image")},
        {"title": "Board 2", "project": Project.objects.get(title="Project 1")},
    ]

    # Create and save Board instances
    for board_data in boards_data:
        board, created = Board.objects.get_or_create(
            title=board_data['title'],
            project=board_data['project']
        )
        if created:
            print(f"Created Board: {board.title}")
        else:
            print(f"Board already exists: {board.title}")

    # Sample data for lists
    print("Completed board creation.")
    lists_data = [
        {"title": "List 1", "board": Board.objects.get(title="Board 1")},
        {"title": "List 2", "board": Board.objects.get(title="Board 2")},
    ]

    # Create and save List instances
    for list_data in lists_data:
        list_instance, created = List.objects.get_or_create(
            title=list_data['title'],
            board=list_data['board']
        )
        if created:
            print(f"Created List: {list_instance.title}")
        else:
            print(f"List already exists: {list_instance.title}")

    # Sample data for tasks
    print("Completed list creation.")
    tasks_data = [
        {"title": "Task 1", "list": List.objects.get(title="List 1"), "story_points": 5},
        {"title": "Task 2", "list": List.objects.get(title="List 2"), "story_points": 10},
    ]

    # Create and save Task instances
    for task_data in tasks_data:
        task, created = Task.objects.get_or_create(
            title=task_data['title'],
            list=task_data['list'],
            defaults={"story_points": task_data['story_points']}  # Provide story_points here
        )
        if created:
            print(f"Created Task: {task.title}")
        else:
            print(f"Task already exists: {task.title}")

    print("Sample data import finished.")

# Optional: Create a function to run this sample data import
def run_sample_data():
    sample_data()
