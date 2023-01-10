# Generated by Django 4.1.5 on 2023-01-05 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_rename_name_listing_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='listing_id',
            new_name='listing',
        ),
        migrations.RenameField(
            model_name='bid',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='listing_id',
            new_name='listing',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='watchlist',
            old_name='listing_id',
            new_name='listing',
        ),
        migrations.RenameField(
            model_name='watchlist',
            old_name='user_id',
            new_name='user',
        ),
    ]
