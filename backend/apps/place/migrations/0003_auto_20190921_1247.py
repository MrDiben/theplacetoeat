# Generated by Django 2.2.5 on 2019-09-21 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_auto_20190921_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='is_closed',
            new_name='is_active',
        ),
    ]