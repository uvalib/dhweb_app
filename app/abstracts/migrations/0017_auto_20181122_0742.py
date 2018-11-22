# Generated by Django 2.1 on 2018-11-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0016_auto_20181122_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appellation',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='appellation',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='conferenceseries',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='end_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='start_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='version',
            name='full_text',
            field=models.TextField(blank=True, max_length=50000, null=True),
        ),
    ]
