# Generated by Django 3.2.3 on 2021-05-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=50, null=True)),
                ('min_salary', models.IntegerField()),
                ('max_salary', models.IntegerField()),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
    ]