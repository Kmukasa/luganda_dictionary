# Generated by Django 3.0.6 on 2020-05-04 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_auto_20200504_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='down_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='up_votes',
            field=models.IntegerField(default=0),
        ),
    ]