# Generated by Django 2.1 on 2018-11-09 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0004_conference_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='full_text',
            field=models.TextField(max_length=50000, null=True),
        ),
    ]
