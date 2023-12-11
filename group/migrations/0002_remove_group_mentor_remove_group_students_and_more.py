# Generated by Django 5.0 on 2023-12-11 21:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='group',
            name='students',
        ),
        migrations.AddField(
            model_name='group',
            name='mentor',
            field=models.ManyToManyField(blank=True, related_name='mentor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
    ]
