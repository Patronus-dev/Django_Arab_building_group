# Generated by Django 5.0.6 on 2024-06-20 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_active_alter_project_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='image',
            new_name='image_cover',
        ),
        migrations.RenameField(
            model_name='projectphoto',
            old_name='image',
            new_name='image_gallery',
        ),
    ]
