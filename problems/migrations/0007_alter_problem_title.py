# Generated by Django 3.2.7 on 2021-09-22 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0006_alter_problem_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
