# Generated by Django 3.1.5 on 2021-02-10 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_auto_20210210_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fllowers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='user',
            name='following',
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fllowing', to=settings.AUTH_USER_MODEL),
        ),
    ]
