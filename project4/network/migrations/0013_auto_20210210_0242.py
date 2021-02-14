# Generated by Django 3.1.5 on 2021-02-10 02:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_auto_20210210_0241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='_user_followers_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='user',
            name='following',
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, null=True, related_name='_user_following_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
