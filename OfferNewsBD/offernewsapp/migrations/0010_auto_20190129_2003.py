# Generated by Django 2.1.2 on 2019-01-29 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offernewsapp', '0009_auto_20190129_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
