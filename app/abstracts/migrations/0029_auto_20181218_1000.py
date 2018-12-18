# Generated by Django 2.1 on 2018-12-18 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0028_remove_author_appellations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appellationassertion',
            name='appellation',
        ),
        migrations.RemoveField(
            model_name='appellationassertion',
            name='asserted_by',
        ),
        migrations.RemoveField(
            model_name='appellationassertion',
            name='author',
        ),
        migrations.AddField(
            model_name='appellation',
            name='asserted_by',
            field=models.ManyToManyField(related_name='appellation_assertions', to='abstracts.Version'),
        ),
        migrations.AddField(
            model_name='appellation',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='appellations', to='abstracts.Author'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AppellationAssertion',
        ),
    ]
