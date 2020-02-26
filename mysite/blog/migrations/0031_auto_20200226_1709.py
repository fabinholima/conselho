# Generated by Django 3.0.3 on 2020-02-26 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20200225_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, unique_for_date='created_on'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publicar')], default=1),
        ),
    ]
