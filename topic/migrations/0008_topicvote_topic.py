# Generated by Django 2.0.2 on 2018-03-02 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0007_auto_20180302_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='topicvote',
            name='topic',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='topic.Topic', verbose_name='Topic'),
            preserve_default=False,
        ),
    ]