# Generated by Django 4.2.5 on 2023-11-22 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userpins'),
    ]

    operations = [
        migrations.CreateModel(
            name='commets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=40)),
                ('pinid', models.CharField(max_length=40)),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
