from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db.models import Q

class Project(models.Model):
    title = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256, blank=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True) 
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only for new projects
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Board(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='boards')
    title = models.CharField(max_length=64)

    class Meta:
        unique_together = ('project', 'title')

    def __str__(self):
        return self.title

class List(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')
    title = models.CharField(max_length=64)
    position = models.IntegerField()

    class Meta:
        unique_together = ('board', 'title')
        constraints = [
            models.CheckConstraint(check=models.Q(position__gte=0), name="position_gte_0")
        ]

    def __str__(self):
        return self.title

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]
    
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512, blank=True)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    story_points = models.IntegerField()

    def clean(self):
        if self.story_points < 0 or self.story_points > 100:
            raise ValidationError("Story points must be between 0 and 100.")
        if self.story_points % 5 != 0:
            raise ValidationError("Story points must be a multiple of 5.")

    def save(self, *args, **kwargs):
        self.clean()  # Call clean method to enforce validation
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Label(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='labels')
    title = models.CharField(max_length=32)
    color = models.CharField(max_length=7, validators=[
        RegexValidator(regex=r'^#[A-Fa-f0-9]{6}$', message="Color must be a valid hex code.")
    ])  # This will store hex color codes like #FFFFFF

    class Meta:
        unique_together = ('project', 'title')

    def __str__(self):
        return f"{self.title} ({self.color})"
