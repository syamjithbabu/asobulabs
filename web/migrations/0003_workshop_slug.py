# Generated by Django 5.1.2 on 2024-10-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_workshop_image1_workshop_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
