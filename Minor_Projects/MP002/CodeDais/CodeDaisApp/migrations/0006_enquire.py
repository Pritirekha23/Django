# Generated by Django 5.0.6 on 2024-06-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeDaisApp', '0005_rename_img_trainers_imgt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('msg', models.TextField()),
            ],
        ),
    ]
