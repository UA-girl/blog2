# Generated by Django 3.0.6 on 2020-06-02 08:31

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200528_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.upload_user_image),
        ),
    ]
