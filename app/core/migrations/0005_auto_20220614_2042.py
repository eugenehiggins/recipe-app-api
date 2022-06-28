# Generated by Django 3.2.13 on 2022-06-14 20:42

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220614_0225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='price',
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=core.models.recipe_image_file_path),
        ),
    ]
