# Generated by Django 5.0.6 on 2024-06-03 15:17

import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
                ('code', models.CharField(max_length=100, unique=True, verbose_name='角色编码')),
                ('order', models.IntegerField(default=0, verbose_name='排序')),
                ('enable', models.BooleanField(default=True, verbose_name='启用')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
