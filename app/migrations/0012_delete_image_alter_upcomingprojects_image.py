# Generated by Django 5.0.4 on 2024-05-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_upcomingprojects_image_upcomingprojects_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AlterField(
            model_name='upcomingprojects',
            name='image',
            field=models.ImageField(upload_to='upcoming_projects/'),
        ),
    ]
