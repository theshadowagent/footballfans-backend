# Generated by Django 3.0.9 on 2020-08-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='photo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
