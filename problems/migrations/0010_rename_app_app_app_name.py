# Generated by Django 3.2.7 on 2021-10-11 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0009_problem_app'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app',
            old_name='app',
            new_name='app_name',
        ),
    ]
