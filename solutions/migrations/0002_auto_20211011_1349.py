# Generated by Django 3.2.7 on 2021-10-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='solution',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='solution',
            name='test_solution',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
