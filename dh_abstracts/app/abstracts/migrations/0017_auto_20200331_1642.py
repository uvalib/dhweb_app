# Generated by Django 3.0.4 on 2020-03-31 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0016_auto_20200330_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='venue',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='conference',
            name='venue_abbreviation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='conferenceseries',
            name='abbreviation',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='conferenceseries',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
