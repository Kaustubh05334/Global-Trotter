# Generated by Django 4.2.1 on 2023-07-11 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(blank=True, choices=[('destination', 'Destination'), ('hotels', 'Hotels'), ('travel', 'Travel'), ('lifestyle', 'Lifestyle'), ('airline', 'Airline')], max_length=20, null=True),
        ),
    ]
