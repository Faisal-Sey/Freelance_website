# Generated by Django 3.1 on 2021-08-04 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20210804_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetails',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
