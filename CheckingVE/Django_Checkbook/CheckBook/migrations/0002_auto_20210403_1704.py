# Generated by Django 3.1.7 on 2021-04-03 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CheckBook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='startingBalance',
            new_name='initial_deposit',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
