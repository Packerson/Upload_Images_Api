# Generated by Django 4.1.7 on 2023-03-06 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0012_rename_image_other_image_image_custom'),
        ('links', '0005_remove_links_user_alter_links_expiration_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='link',
        ),
        migrations.AddField(
            model_name='links',
            name='image',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='link_image', to='images.image'),
        ),
    ]
