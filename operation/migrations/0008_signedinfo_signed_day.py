# Generated by Django 2.0.2 on 2018-03-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0007_auto_20180313_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='signedinfo',
            name='signed_day',
            field=models.IntegerField(default=0, verbose_name='连续签到天数'),
        ),
    ]