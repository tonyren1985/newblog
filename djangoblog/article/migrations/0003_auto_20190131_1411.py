# Generated by Django 2.1.5 on 2019-01-31 06:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190131_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 31, 6, 11, 17, 460336, tzinfo=utc)),
        ),
    ]
