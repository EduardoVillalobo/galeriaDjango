# Generated by Django 4.1.4 on 2022-12-28 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_photo_foto_photo_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 28, 11, 4, 54, 80569, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
