# Generated by Django 3.2.7 on 2021-09-21 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_auto_20210920_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.app')),
            ],
        ),
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause', models.TextField(blank=True, null=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.problemtype')),
            ],
        ),
    ]