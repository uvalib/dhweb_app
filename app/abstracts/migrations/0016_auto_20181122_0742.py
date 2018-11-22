# Generated by Django 2.1 on 2018-11-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0015_auto_20181120_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appellationassertion',
            name='asserted_by',
        ),
        migrations.AddField(
            model_name='appellationassertion',
            name='asserted_by',
            field=models.ManyToManyField(related_name='appellation_assertions', to='abstracts.Version'),
        ),
        migrations.RemoveField(
            model_name='departmentassertion',
            name='asserted_by',
        ),
        migrations.AddField(
            model_name='departmentassertion',
            name='asserted_by',
            field=models.ManyToManyField(related_name='department_assertions', to='abstracts.Version'),
        ),
        migrations.RemoveField(
            model_name='genderassertion',
            name='asserted_by',
        ),
        migrations.AddField(
            model_name='genderassertion',
            name='asserted_by',
            field=models.ManyToManyField(related_name='gender_assertions', to='abstracts.Version'),
        ),
        migrations.RemoveField(
            model_name='institutionassertion',
            name='asserted_by',
        ),
        migrations.AddField(
            model_name='institutionassertion',
            name='asserted_by',
            field=models.ManyToManyField(related_name='institution_assertions', to='abstracts.Version'),
        ),
    ]
