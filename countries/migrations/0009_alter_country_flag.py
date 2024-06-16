# Generated by Django 5.0.6 on 2024-06-15 17:51

import countries.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0008_alter_landmark_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='flag',
            field=models.ImageField(default='default_flag.png', upload_to=countries.models.Country.custom_upload),
        ),
    ]
