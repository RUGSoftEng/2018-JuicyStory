# Generated by Django 2.0.3 on 2018-03-27 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_merge_20180326_1241'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InstagramClient',
        ),
    ]