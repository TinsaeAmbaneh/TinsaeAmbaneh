# Generated by Django 4.2.2 on 2023-06-23 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='vedio',
            new_name='video',
        ),
    ]
