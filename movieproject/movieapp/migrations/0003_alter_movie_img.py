# Generated by Django 5.0.4 on 2024-05-17 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
