# Generated by Django 2.1.2 on 2019-01-28 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offernewsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='AuthorId',
            new_name='author',
        ),
    ]