# Generated by Django 3.2.7 on 2022-01-27 10:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cittu_report', '0002_alter_subunitreport_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='subunitreport',
            name='achievement',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='subunitreport',
            name='challenge',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='subunitreport',
            name='conclusion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='subunitreport',
            name='introduction',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='subunitreport',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]