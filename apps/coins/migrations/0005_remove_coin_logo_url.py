# Generated by Django 3.2.6 on 2021-08-21 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0004_alter_coin_logo_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coin',
            name='logo_url',
        ),
    ]
