# Generated by Django 4.2.1 on 2023-06-19 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0015_blogpost_likes_delete_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255)),
                ('report_type', models.CharField(choices=[('harassment', 'Harassment'), ('bullying', 'Bullying'), ('harmful', 'Harmful Content'), ('sexual', 'Sexual Content'), ('child_abuse', 'Child Abuse'), ('spam', 'Spam')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('resolved_status', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogpost')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
