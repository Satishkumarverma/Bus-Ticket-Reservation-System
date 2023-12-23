# Generated by Django 4.2.7 on 2023-12-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0007_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='arrivaltime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='busname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='busnumber',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='deparchertime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='destination',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='durition',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='source',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
