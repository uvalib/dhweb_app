# Generated by Django 3.0.5 on 2020-05-01 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0051_auto_20200430_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='attendance',
            field=models.TextField(blank=True, default='', help_text='Summary information about conference attendance, with source links', max_length=20000),
        ),
        migrations.AlterField(
            model_name='conference',
            name='contributors',
            field=models.TextField(blank=True, default='', help_text='Individuals or organizations who contributed data about this conference', max_length=20000),
        ),
        migrations.AlterField(
            model_name='conference',
            name='notes',
            field=models.TextField(blank=True, default='', help_text='Further descriptive information', max_length=200000),
        ),
        migrations.AlterField(
            model_name='conference',
            name='references',
            field=models.TextField(blank=True, default='', help_text='Citations to conference proceedings', max_length=20000),
        ),
    ]
