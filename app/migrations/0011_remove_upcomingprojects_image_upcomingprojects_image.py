# Generated by Django 5.0.4 on 2024-05-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_image_remove_upcomingprojects_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upcomingprojects',
            name='image',
        ),
        migrations.AddField(
            model_name='upcomingprojects',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upcoming_projects/'),
        ),
    ]
