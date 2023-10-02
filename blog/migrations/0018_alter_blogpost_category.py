# Generated by Django 4.2.1 on 2023-07-11 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('destination', 'Destination'), ('hotels', 'Hotels'), ('travel', 'Travel'), ('lifestyle', 'Lifestyle'), ('airline', 'Airline')], default='destination', max_length=20),
        ),
    ]