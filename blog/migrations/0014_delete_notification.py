# Generated by Django 4.2.1 on 2023-06-07 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_notification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
