# Generated by Django 2.1 on 2018-12-18 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0027_auto_20181217_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='appellations',
        ),
    ]
