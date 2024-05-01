# Generated by Django 5.0.4 on 2024-05-01 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_enquiry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enquiry',
            options={'ordering': ['name'], 'verbose_name': 'Enquiry', 'verbose_name_plural': 'Enquiries'},
        ),
        migrations.AlterUniqueTogether(
            name='enquiry',
            unique_together={('name', 'email')},
        ),
    ]
