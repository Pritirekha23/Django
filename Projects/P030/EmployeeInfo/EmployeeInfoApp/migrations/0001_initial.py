# Generated by Django 5.0.6 on 2024-06-25 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desg', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('sal', models.FloatField()),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
