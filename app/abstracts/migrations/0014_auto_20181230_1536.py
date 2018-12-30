# Generated by Django 2.1 on 2018-12-30 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0013_auto_20181230_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='disciplines',
            field=models.ManyToManyField(blank=True, related_name='works', to='abstracts.Discipline'),
        ),
        migrations.AlterField(
            model_name='work',
            name='keywords',
            field=models.ManyToManyField(blank=True, related_name='works', to='abstracts.Keyword'),
        ),
        migrations.AlterField(
            model_name='work',
            name='languages',
            field=models.ManyToManyField(blank=True, related_name='works', to='abstracts.Language'),
        ),
        migrations.AlterField(
            model_name='work',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='works', to='abstracts.Topic'),
        ),
    ]
