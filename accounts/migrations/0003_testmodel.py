# Generated by Django 4.2.1 on 2023-05-13 10:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_email_remove_profile_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test1', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
