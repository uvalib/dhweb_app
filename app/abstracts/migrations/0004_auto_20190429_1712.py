# Generated by Django 2.1 on 2019-04-29 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0003_auto_20190428_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['pref_name']},
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'ordering': ['title']},
        ),
        migrations.RemoveIndex(
            model_name='work',
            name='abstracts_w_search__cfd9ce_gin',
        ),
    ]
