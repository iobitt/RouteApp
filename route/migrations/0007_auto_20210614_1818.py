# Generated by Django 3.2.4 on 2021-06-14 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0006_auto_20210614_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
