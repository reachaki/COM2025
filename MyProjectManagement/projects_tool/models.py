from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.utils import timezone



class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='project_images/', blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)    # Temporarily allow null values


    def clean(self):
        if not self.title:
            raise ValidationError("Title cannot be blank.")
        if len(self.title) > 64:
            raise ValidationError("Title cannot exceed 64 characters.")

    def save(self, *args, **kwargs):
        self.clean()  # Call clean method to enforce validation
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug__iexact=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Board(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='boards')
    title = models.CharField(max_length=64)

    class Meta:
        unique_together = ('project', 'title')

    def clean(self):
        if not self.title:
            raise ValidationError("Title cannot be blank.")
        if len(self.title) > 64:
            raise ValidationError("Title cannot exceed 64 characters.")

    def __str__(self):
        return self.title


class List(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')  # Added ForeignKey to Board
    title = models.CharField(max_length=64)
    position = models.IntegerField(null=True)  # Removed duplicate definition

    class Meta:
        unique_together = ('board', 'title')
        constraints = [
            models.CheckConstraint(check=models.Q(position__gte=0), name="position_gte_0")
        ]

    def clean(self):
        if not self.title:
            raise ValidationError("Title cannot be blank.")
        if len(self.title) > 64:
            raise ValidationError("Title cannot exceed 64 characters.")

    def __str__(self):
        return self.title


# Separate validator for story points
def validate_story_points(value):
    if value < 0 or value > 100 or value % 5 != 0:
        raise ValidationError(f"{value} is not a valid story point. Must be between 0 and 100, and a multiple of 5.")


class Task(models.Model):
    class Priority(models.TextChoices):
        HIGH = 'HIGH', _('High')
        MEDIUM = 'MEDIUM', _('Medium')
        LOW = 'LOW', _('Low')

    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=512, blank=True)
    priority = models.CharField(max_length=6, choices=Priority.choices, default=Priority.MEDIUM)
    story_points = models.PositiveIntegerField(validators=[validate_story_points])
    labels = models.ManyToManyField('Label', blank=True)

    def clean(self):
        if not self.title:
            raise ValidationError("Title cannot be blank.")
        if len(self.title) > 64:
            raise ValidationError("Title cannot exceed 64 characters.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Label(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='labels')
    title = models.CharField(max_length=32)
    color = models.CharField(max_length=7, validators=[
        RegexValidator(regex=r'^#[A-Fa-f0-9]{6}$', message="Color must be a valid hex code.")
    ])

    class Meta:
        unique_together = ('project', 'title')

    def clean(self):
        if not self.title:
            raise ValidationError("Title cannot be blank.")
        if len(self.title) > 32:
            raise ValidationError("Title cannot exceed 32 characters.")

    def __str__(self):
        return f"{self.title} ({self.color})"


