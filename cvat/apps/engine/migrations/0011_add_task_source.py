# Generated by Django 2.0.9 on 2018-10-24 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0010_auto_20181011_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='source',
            field=models.CharField(default='unknown', max_length=256),
        ),
    ]
