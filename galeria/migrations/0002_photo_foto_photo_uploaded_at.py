# Generated by Django 4.1.4 on 2022-12-27 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='foto',
            field=models.FileField(default=datetime.datetime(2022, 12, 27, 12, 44, 54, 624647, tzinfo=datetime.timezone.utc), upload_to='fotos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 12, 27, 12, 45, 44, 456873, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
