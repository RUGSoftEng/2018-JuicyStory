# Generated by Django 2.0.2 on 2018-03-23 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authcode', '0004_auto_20180323_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selectedimage',
            old_name='username',
            new_name='instagram_user',
        ),
    ]