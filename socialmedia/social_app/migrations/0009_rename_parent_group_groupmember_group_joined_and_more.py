# Generated by Django 4.2.4 on 2023-08-25 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social_app', '0008_rename_is_admin_groupmember_is_group_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupmember',
            old_name='parent_group',
            new_name='group_joined',
        ),
        migrations.CreateModel(
            name='SharedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_shared', models.DateTimeField(auto_now_add=True)),
                ('original_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_app.userpost')),
                ('shared_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
