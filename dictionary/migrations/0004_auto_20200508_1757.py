# Generated by Django 3.0.6 on 2020-05-08 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_auto_20200504_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='english_word',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='luganda_word',
            field=models.CharField(max_length=100),
        ),
    ]