# Generated by Django 4.1.7 on 2023-03-03 18:13

import apps.images.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0005_alter_image_image_200_alter_image_image_400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_200',
            field=models.ImageField(blank=True, null=True, upload_to=apps.images.models.user_directory_path_200),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_400',
            field=models.ImageField(blank=True, null=True, upload_to=apps.images.models.user_directory_path_400),
        ),
        migrations.AlterField(
            model_name='image',
            name='plan',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plan', to='profiles.profile'),
        ),
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image', to=settings.AUTH_USER_MODEL),
        ),
    ]
