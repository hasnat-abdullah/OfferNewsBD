# Generated by Django 2.1.2 on 2019-02-07 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offernewsapp', '0012_post_badgetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='badgeType',
            field=models.CharField(choices=[('NEW', 'New'), ('HOT', 'Hot'), ('EXPIRED', 'Expired')], default='NEW', max_length=7),
        ),
    ]