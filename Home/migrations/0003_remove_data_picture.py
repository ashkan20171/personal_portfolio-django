# Generated by Django 3.0.5 on 2020-04-30 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_data_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='picture',
        ),
    ]
