# Generated by Django 3.0.3 on 2020-02-23 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200223_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='height',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='width',
            field=models.IntegerField(default=True),
        ),
    ]