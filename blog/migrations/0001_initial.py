# Generated by Django 5.0.6 on 2024-06-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='blog/blog_cover/', verbose_name='blog Image')),
                ('status', models.CharField(choices=[('pub', 'published'), ('drf', 'draft')], max_length=3)),
            ],
        ),
    ]
