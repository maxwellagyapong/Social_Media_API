# Generated by Django 4.2.4 on 2023-08-24 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupmember',
            options={'verbose_name_plural': 'Group Members'},
        ),
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name_plural': 'Replies'},
        ),
        migrations.AlterModelOptions(
            name='userpost',
            options={'verbose_name_plural': 'Posts'},
        ),
    ]