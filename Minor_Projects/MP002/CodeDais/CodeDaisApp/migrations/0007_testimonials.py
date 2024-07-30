# Generated by Django 5.0.6 on 2024-06-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeDaisApp', '0006_enquire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgts', models.ImageField(upload_to='teacher_images/')),
                ('tsname', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]