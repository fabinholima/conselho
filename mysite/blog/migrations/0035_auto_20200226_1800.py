# Generated by Django 3.0.3 on 2020-02-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_auto_20200226_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, unique_for_date='published_date'),
        ),
    ]
