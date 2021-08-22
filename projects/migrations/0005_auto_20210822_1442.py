# Generated by Django 3.2.6 on 2021-08-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_feaured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='feaured_image',
        ),
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]