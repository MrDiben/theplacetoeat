# Generated by Django 2.2.5 on 2019-09-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_auto_20190921_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooktype',
            name='name',
            field=models.CharField(choices=[('ASIATIC', 'Asiatic'), ('AMERICAN', 'American'), ('VEGETARIAN', 'Vegetarian'), ('VEGAN', 'Vegan'), ('FRENCH', 'French'), ('ITALIAN', 'Italian'), ('INDIAN', 'Indian'), ('CHINESE', 'Chinese'), ('JAPAN', 'Japan'), ('MEXICAN', 'Mexican'), ('TAPAS', 'Tapas'), ('FISH', 'Fish'), ('MEAT', 'Meat'), ('BIO', 'Bio'), ('FASTFOOD', 'Fastfood')], max_length=20),
        ),
    ]
