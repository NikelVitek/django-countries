# Generated by Django 5.0.6 on 2024-06-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_remove_country_flag_landmark_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='flag',
            field=models.ImageField(blank=True, null=True, upload_to='flags/'),
        ),
    ]
