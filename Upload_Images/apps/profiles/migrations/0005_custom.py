# Generated by Django 4.1.7 on 2023-03-04 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom', to='profiles.profile')),
            ],
        ),
    ]