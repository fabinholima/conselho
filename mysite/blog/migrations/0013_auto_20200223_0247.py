# Generated by Django 3.0.3 on 2020-02-23 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200223_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='caption_image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='height',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', height_field='height', upload_to='static/blog/uploads/%Y/%m/%d/', width_field='width'),
        ),
        migrations.AddField(
            model_name='post',
            name='width',
            field=models.PositiveIntegerField(null=True),
        ),
    ]