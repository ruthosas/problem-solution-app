# Generated by Django 3.2.7 on 2021-10-20 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0010_rename_app_app_app_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='answered',
            field=models.BooleanField(default=False),
        ),
    ]
