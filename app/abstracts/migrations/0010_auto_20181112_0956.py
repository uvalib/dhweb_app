# Generated by Django 2.1 on 2018-11-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0009_auto_20181112_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seriesmembership',
            name='number',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
