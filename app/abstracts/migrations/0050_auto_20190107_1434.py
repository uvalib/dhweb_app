# Generated by Django 2.1 on 2019-01-07 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0049_auto_20190107_0934'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='institution',
            unique_together={('name', 'country')},
        ),
    ]
