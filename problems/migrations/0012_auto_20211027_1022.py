# Generated by Django 3.2.7 on 2021-10-27 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0011_problem_answered'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem',
            old_name='answered',
            new_name='adopted',
        ),
        migrations.AddField(
            model_name='problem',
            name='attempted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='problem',
            name='location',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='problems.location'),
            preserve_default=False,
        ),
    ]