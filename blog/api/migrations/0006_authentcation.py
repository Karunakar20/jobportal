# Generated by Django 5.1.6 on 2025-02-12 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_portalusers_is_recruiter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authentcation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_login', models.BooleanField(default=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_fk_users', to='api.portalusers')),
            ],
            options={
                'db_table': 'db_auth',
            },
        ),
    ]
