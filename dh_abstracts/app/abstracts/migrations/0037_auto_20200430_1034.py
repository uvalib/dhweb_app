# Generated by Django 3.0.5 on 2020-04-30 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0036_auto_20200429_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizer',
            name='abbreviation',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
