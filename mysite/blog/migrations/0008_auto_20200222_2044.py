# Generated by Django 3.0.3 on 2020-02-22 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='parent',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]