# Generated by Django 4.0.3 on 2022-04-05 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IplTeam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='facebool_link',
            new_name='facebook_link',
        ),
    ]
