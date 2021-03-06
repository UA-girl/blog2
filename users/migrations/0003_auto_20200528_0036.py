# Generated by Django 3.0.6 on 2020-05-27 21:36

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200523_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='users/user_empty_photo.jpg', null=True, upload_to=users.models.upload_user_image),
        ),
    ]
