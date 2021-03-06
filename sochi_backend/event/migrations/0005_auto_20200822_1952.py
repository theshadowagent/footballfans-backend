# Generated by Django 3.0.9 on 2020-08-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20200822_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_home_event',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
