# Generated by Django 2.0.2 on 2018-04-28 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagramuser',
            name='fbid',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='instagramuser',
            name='fbtoken',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]