# Generated by Django 5.0.4 on 2024-06-04 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_gallery_options'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enquiry',
            unique_together=set(),
        ),
    ]
