# Generated by Django 2.1.2 on 2019-02-12 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offernewsapp', '0014_auto_20190212_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featuredpost',
            name='postId',
        ),
        migrations.AddField(
            model_name='featuredpost',
            name='postId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='offernewsapp.Post'),
            preserve_default=False,
        ),
    ]