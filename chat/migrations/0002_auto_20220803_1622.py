# Generated by Django 3.1.1 on 2022-08-03 11:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='chat/'),
        ),
        migrations.AddField(
            model_name='chat',
            name='is_archived',
            field=models.ManyToManyField(related_name='user_archived', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='is_group',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chat',
            name='pinned',
            field=models.ManyToManyField(related_name='user_pinned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='chat',
            name='unmuted',
            field=models.ManyToManyField(related_name='user_unmuted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='read',
            field=models.ManyToManyField(related_name='user_read', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chat',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
