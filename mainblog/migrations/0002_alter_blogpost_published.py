# Generated by Django 5.0.6 on 2024-06-11 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='published',
            field=models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=0, verbose_name='Опубликовать'),
        ),
    ]
