# Generated by Django 4.2.5 on 2023-09-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userpins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=40)),
                ('userid', models.CharField(max_length=40)),
                ('pin', models.ImageField(upload_to='pins/')),
            ],
        ),
    ]
