# Generated by Django 5.1.1 on 2024-09-16 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='reting',
            new_name='rating',
        ),
    ]
