# Generated by Django 2.1.5 on 2019-01-29 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_userinfo_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
