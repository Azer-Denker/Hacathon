# Generated by Django 2.2.13 on 2021-11-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_authtoken_self'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authtoken',
            name='self',
        ),
        migrations.AddField(
            model_name='profile',
            name='self',
            field=models.TextField(default='None', max_length=300, verbose_name='О себе'),
        ),
    ]
