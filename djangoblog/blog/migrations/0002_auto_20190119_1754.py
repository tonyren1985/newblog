# Generated by Django 2.1.5 on 2019-01-19 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogarticles',
            old_name='anthor',
            new_name='author',
        ),
    ]
