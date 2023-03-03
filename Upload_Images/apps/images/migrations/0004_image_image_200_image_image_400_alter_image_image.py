# Generated by Django 4.1.7 on 2023-03-03 16:31

import apps.images.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_image_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_200',
            field=models.ImageField(null=True, upload_to=apps.images.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='image',
            name='image_400',
            field=models.ImageField(null=True, upload_to=apps.images.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to=apps.images.models.user_directory_path),
        ),
    ]
