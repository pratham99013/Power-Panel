# Generated by Django 5.0.4 on 2024-06-18 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_reply_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='photo',
        ),
        migrations.AddField(
            model_name='question',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
