# Generated by Django 2.1 on 2018-11-09 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appellation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppellationAssertion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appellation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assertions', to='abstracts.Appellation')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Authorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorship_order', models.IntegerField(default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorships', to='abstracts.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('venue', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentAssertion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GenderAssertion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionAssertion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(max_length=100, null=True)),
                ('start_date', models.CharField(max_length=100, null=True)),
                ('end_date', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True)),
                ('submission_type', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(choices=[('ac', 'accpeted'), ('su', 'submission')], max_length=2)),
                ('full_text', models.CharField(max_length=50000, null=True)),
                ('tags', models.ManyToManyField(related_name='versions', to='abstracts.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to='abstracts.Conference')),
            ],
        ),
        migrations.AddField(
            model_name='version',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='abstracts.Work'),
        ),
        migrations.AddField(
            model_name='institutionassertion',
            name='asserted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institution_assertions', to='abstracts.Version'),
        ),
        migrations.AddField(
            model_name='institutionassertion',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institution_memberships', to='abstracts.Author'),
        ),
        migrations.AddField(
            model_name='institutionassertion',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assertions', to='abstracts.Institution'),
        ),
        migrations.AddField(
            model_name='genderassertion',
            name='asserted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gender_assertions', to='abstracts.Version'),
        ),
        migrations.AddField(
            model_name='genderassertion',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gender_memberships', to='abstracts.Author'),
        ),
        migrations.AddField(
            model_name='genderassertion',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gender_authors', to='abstracts.Gender'),
        ),
        migrations.AddField(
            model_name='departmentassertion',
            name='asserted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_assertions', to='abstracts.Version'),
        ),
        migrations.AddField(
            model_name='departmentassertion',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_memberships', to='abstracts.Author'),
        ),
        migrations.AddField(
            model_name='departmentassertion',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assertions', to='abstracts.Department'),
        ),
        migrations.AddField(
            model_name='department',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='abstracts.Institution'),
        ),
        migrations.AddField(
            model_name='authorship',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorships', to='abstracts.Version'),
        ),
        migrations.AddField(
            model_name='appellationassertion',
            name='asserted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appellation_assertions', to='abstracts.Version'),
        ),
        migrations.AddField(
            model_name='appellationassertion',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appellation_assertions', to='abstracts.Author'),
        ),
    ]
