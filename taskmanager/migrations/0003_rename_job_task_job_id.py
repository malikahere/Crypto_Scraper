# Generated by Django 5.0.6 on 2024-06-10 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_job_coins'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='job',
            new_name='job_id',
        ),
    ]
