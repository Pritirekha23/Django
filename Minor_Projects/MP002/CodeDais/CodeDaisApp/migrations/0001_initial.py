# Generated by Django 5.0.6 on 2024-06-29 09:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='course_images/', validators=[django.core.validators.validate_image_file_extension])),
                ('logo_duration', models.ImageField(upload_to='course_logos/', validators=[django.core.validators.validate_image_file_extension])),
                ('logo_lessons', models.ImageField(upload_to='course_logos/', validators=[django.core.validators.validate_image_file_extension])),
                ('logo_enrolled', models.ImageField(upload_to='course_logos/', validators=[django.core.validators.validate_image_file_extension])),
                ('cname', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('lessons', models.CharField(max_length=50)),
                ('enrolled', models.CharField(max_length=50)),
                ('course_type', models.CharField(max_length=50)),
                ('button_link', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
