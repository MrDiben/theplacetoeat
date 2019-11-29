# Generated by Django 2.2.6 on 2019-11-22 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0006_auto_20191011_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='price_indicator',
            field=models.CharField(choices=[('€€€', '€€€'), ('€€', '€€'), ('€', '€')], default='€€', max_length=3, verbose_name='Price Indicator'),
        ),
    ]
