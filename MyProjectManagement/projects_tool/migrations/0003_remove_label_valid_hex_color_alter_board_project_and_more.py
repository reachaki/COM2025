# Generated by Django 5.1.1 on 2024-10-18 14:21

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_tool', '0002_alter_project_image'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='label',
            name='valid_hex_color',
        ),
        migrations.AlterField(
            model_name='board',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='projects_tool.project'),
        ),
        migrations.AlterField(
            model_name='label',
            name='color',
            field=models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(message='Color must be a valid hex code.', regex='^#[A-Fa-f0-9]{6}$')]),
        ),
        migrations.AlterField(
            model_name='label',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='projects_tool.project'),
        ),
        migrations.AlterField(
            model_name='list',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='projects_tool.board'),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='projects_tool.list'),
        ),
    ]
