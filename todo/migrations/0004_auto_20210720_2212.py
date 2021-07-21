# Generated by Django 3.2.5 on 2021-07-20 20:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_content_createdat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='desc',
        ),
        migrations.AddField(
            model_name='content',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='content',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
