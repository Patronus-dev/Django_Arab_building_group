# Generated by Django 5.0.6 on 2024-06-20 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='project',
            name='address',
            field=models.TextField(max_length=100, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_construction',
            field=models.IntegerField(blank=True, default=2024, null=True, verbose_name='date construction'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=700, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='project/project_cover/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='project',
            name='minus_floor',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='floors underground'),
        ),
        migrations.AlterField(
            model_name='project',
            name='plus_floor',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='floors on ground'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='project',
            name='unit_meterage',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='meterage'),
        ),
        migrations.AlterField(
            model_name='project',
            name='units',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='units'),
        ),
        migrations.AlterField(
            model_name='project',
            name='units_in_floor',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='units in each floor'),
        ),
    ]
