# Generated by Django 5.0.6 on 2024-05-29 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=30)),
                ('mark', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
