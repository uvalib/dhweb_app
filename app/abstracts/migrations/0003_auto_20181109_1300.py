# Generated by Django 2.1 on 2018-11-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0002_auto_20181109_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='conference',
            name='organizers',
            field=models.ManyToManyField(related_name='conferences_organized', to='abstracts.Organizer'),
        ),
    ]
