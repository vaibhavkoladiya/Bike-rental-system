# Generated by Django 3.1.5 on 2021-02-03 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bikerental', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bikerental.user')),
                ('mobile_no', models.DecimalField(decimal_places=0, default='1234567890', max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='DealerProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bikerental.user')),
                ('profile_pic', models.ImageField(default='default.jpg', upload_to='profile_pics')),
            ],
        ),
    ]
