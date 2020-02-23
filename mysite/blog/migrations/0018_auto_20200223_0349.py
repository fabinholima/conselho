# Generated by Django 3.0.3 on 2020-02-23 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200223_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/blog/uploads/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
