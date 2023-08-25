# Generated by Django 4.2.4 on 2023-08-25 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0003_alter_groupmember_options_alter_userpost_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commment',
            name='parent_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='social_app.userpost'),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='group_joined',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_members', to='social_app.group'),
        ),
        migrations.AlterField(
            model_name='like',
            name='parent_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='social_app.userpost'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='parent_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='social_app.commment'),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='media_file',
            field=models.FileField(blank=True, null=True, upload_to='media/posts-media'),
        ),
    ]