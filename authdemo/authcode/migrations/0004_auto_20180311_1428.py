# Generated by Django 2.0.3 on 2018-03-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authcode', '0003_auto_20180309_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramuser',
            name='access_token',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
