# Generated by Django 3.1.5 on 2021-02-03 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0002_auto_20210203_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]