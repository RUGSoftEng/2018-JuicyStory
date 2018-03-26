# Generated by Django 2.0.2 on 2018-03-23 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authcode', '0002_instagramuser_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectedImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(max_length=300)),
                ('username', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='authcode.InstagramUser')),
            ],
        ),
    ]