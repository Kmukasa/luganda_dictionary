# Generated by Django 2.2.5 on 2019-11-27 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_word', models.CharField(max_length=250)),
                ('luganda_word', models.CharField(max_length=250)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('up_votes', models.IntegerField()),
                ('down_votes', models.IntegerField()),
            ],
        ),
    ]
