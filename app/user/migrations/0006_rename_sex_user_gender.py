# Generated by Django 3.2.23 on 2024-01-11 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_sex'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='sex',
            new_name='gender',
        ),
    ]
