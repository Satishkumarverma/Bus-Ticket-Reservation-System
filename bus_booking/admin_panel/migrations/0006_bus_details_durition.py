# Generated by Django 4.2.7 on 2023-12-15 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0005_bus_details_availableseats'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus_details',
            name='durition',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
