# Generated by Django 2.1.2 on 2019-01-29 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offernewsapp', '0007_auto_20190128_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='name',
        ),
    ]
