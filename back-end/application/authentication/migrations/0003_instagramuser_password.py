# Generated by Django 2.0.3 on 2018-03-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_instagramuser_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagramuser',
            name='password',
            field=models.CharField(default='%3zf(^u7YX', max_length=50),
            preserve_default=False,
        ),
    ]
