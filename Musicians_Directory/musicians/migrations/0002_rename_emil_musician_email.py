# Generated by Django 4.2.7 on 2024-01-01 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musician',
            old_name='Emil',
            new_name='Email',
        ),
    ]
