# Generated by Django 4.1.7 on 2023-03-02 09:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date_creation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]