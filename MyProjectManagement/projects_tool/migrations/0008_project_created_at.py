# Generated by Django 5.1.1 on 2024-10-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_tool', '0007_alter_list_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
