# Generated by Django 2.1.5 on 2019-01-29 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190129_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='photo',
        ),
    ]
