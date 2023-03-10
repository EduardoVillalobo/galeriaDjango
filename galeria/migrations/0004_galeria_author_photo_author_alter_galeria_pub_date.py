# Generated by Django 4.1.4 on 2023-01-06 12:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galeria', '0003_alter_galeria_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeria',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='galeria',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 12, 25, 12, 823069, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
