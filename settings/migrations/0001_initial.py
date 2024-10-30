# Generated by Django 5.1.1 on 2024-09-23 06:50

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created time')),
                ('updated_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated time')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('value', models.TextField(blank=True, null=True, verbose_name='Value')),
                ('category', models.CharField(default='default', max_length=128, verbose_name='Category')),
                ('encrypted', models.BooleanField(default=False, verbose_name='Encrypted')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
            ],
            options={
                'verbose_name': 'System setting',
                'verbose_name_plural': 'System setting',
            },
        ),
    ]