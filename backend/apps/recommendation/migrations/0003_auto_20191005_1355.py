# Generated by Django 2.2.6 on 2019-10-05 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0002_auto_20191005_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='user.UserProfile', verbose_name='Recommendation'),
        ),
    ]
