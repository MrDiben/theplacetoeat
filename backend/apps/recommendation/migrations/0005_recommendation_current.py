# Generated by Django 2.2.6 on 2019-11-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0004_auto_20191109_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='current',
            field=models.BooleanField(default=False, verbose_name='is current recommendation ?'),
        ),
    ]
