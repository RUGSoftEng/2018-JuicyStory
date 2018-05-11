# Generated by Django 2.0.3 on 2018-03-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('image_file', models.FileField(upload_to='images/%Y/%m/%d')),
            ],
        ),
    ]