# Generated by Django 5.1.6 on 2025-02-11 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_users_poratalusers_alter_poratalusers_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PoratalUsers',
            new_name='PortalUsers',
        ),
    ]
