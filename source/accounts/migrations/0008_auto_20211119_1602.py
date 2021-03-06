# Generated by Django 2.2.13 on 2021-11-19 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20211119_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='git',
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='Ссылка на instagram'),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='Ссылка на linkedin'),
        ),
        migrations.AddField(
            model_name='profile',
            name='telegram',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='Ссылка на telegram'),
        ),
    ]
