# Generated by Django 3.0.6 on 2020-05-04 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Translation',
            new_name='Dictionary',
        ),
    ]
