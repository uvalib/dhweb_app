# Generated by Django 3.0.5 on 2020-05-01 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0053_remove_conference_primary_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='entry_status',
            field=models.CharField(choices=[('n', 'Not started'), ('i', 'Incomplete'), ('c', 'Complete')], db_index=True, default='n', help_text='Have all the abstracts for this conference been entered?', max_length=1),
        ),
    ]
