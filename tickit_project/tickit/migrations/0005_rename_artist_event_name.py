# Generated by Django 4.0 on 2023-07-19 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickit', '0004_event_photo_url_venue_photo_url_alter_event_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='artist',
            new_name='name',
        ),
    ]