# Generated by Django 2.0.3 on 2018-03-09 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=30)),
                ('redirect_uri', models.CharField(max_length=100)),
            ],
        ),
    ]
