# Generated by Django 3.2.6 on 2021-08-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.AddField(
            model_name='profile',
            name='message',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
