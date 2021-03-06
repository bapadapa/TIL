# Generated by Django 3.2.3 on 2021-05-27 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImageUrl', models.CharField(max_length=100)),
                ('seller', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('creatAt', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
    ]
