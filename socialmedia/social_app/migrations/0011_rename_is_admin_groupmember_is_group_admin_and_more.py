# Generated by Django 4.2.4 on 2023-08-25 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0010_rename_is_group_admin_groupmember_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupmember',
            old_name='is_admin',
            new_name='is_group_admin',
        ),
        migrations.RenameField(
            model_name='groupmember',
            old_name='group_joined',
            new_name='parent_group',
        ),
    ]
