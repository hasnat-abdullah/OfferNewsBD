# Generated by Django 2.1.2 on 2019-01-28 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offernewsapp', '0003_auto_20190128_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComFeaturePricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('C', 'Com_Page'), ('F', 'First_Page')], default='F', max_length=1)),
                ('price', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PostFeaturePricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('B', 'Cover_Big'), ('S', 'Cover_Small'), ('F', 'First_Page')], default='F', max_length=1)),
                ('price', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='FeaturePricing',
        ),
        migrations.RemoveField(
            model_name='featured',
            name='featuredType',
        ),
        migrations.RemoveField(
            model_name='featured',
            name='position',
        ),
        migrations.RemoveField(
            model_name='featured',
            name='postId',
        ),
        migrations.AddField(
            model_name='postfeaturepricing',
            name='featuredId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='offernewsapp.Featured'),
        ),
        migrations.AddField(
            model_name='postfeaturepricing',
            name='postId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offernewsapp.Post'),
        ),
        migrations.AddField(
            model_name='comfeaturepricing',
            name='featuredId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='offernewsapp.Featured'),
        ),
        migrations.AddField(
            model_name='comfeaturepricing',
            name='postId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offernewsapp.Post'),
        ),
    ]
