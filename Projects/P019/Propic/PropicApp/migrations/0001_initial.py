# Generated by Django 5.0.6 on 2024-06-07 15:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(upload_to='images/', validators=[django.core.validators.validate_image_file_extension])),
                ('email', models.EmailField(max_length=254)),
                ('mark', models.IntegerField()),
            ],
        ),
    ]
