# Generated by Django 2.2.6 on 2019-11-09 16:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('place', '0006_auto_20191011_1545'),
        ('user', '0003_auto_20191005_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datehour', models.DateTimeField(verbose_name='Meal Date Hour')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_created_meals', to='user.UserProfile', verbose_name='Meal creator')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organised_meals', to='place.Restaurant', verbose_name='Meal Restaurant')),
            ],
            options={
                'unique_together': {('datehour', 'creator')},
            },
        ),
        migrations.CreateModel(
            name='InvitationMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Is Accepted ?')),
                ('note', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='User Note')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='meal.Meal', verbose_name='Meal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_meals', to='user.UserProfile', verbose_name='Invited Meal User')),
            ],
            options={
                'unique_together': {('meal', 'user')},
            },
        ),
    ]
