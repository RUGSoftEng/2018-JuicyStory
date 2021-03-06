# Generated by Django 2.0.2 on 2018-06-06 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_merge_20180514_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='InstagramStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_urls', models.ManyToManyField(to='database.ImageUrl')),
                ('instagram_user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='database.InstagramUser')),
            ],
        ),
    ]
