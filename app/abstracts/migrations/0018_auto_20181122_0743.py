# Generated by Django 2.1 on 2018-11-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0017_auto_20181122_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='submission_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
