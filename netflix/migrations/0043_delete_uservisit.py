# Generated by Django 4.0.3 on 2022-07-20 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0042_remove_white_user_delete_dark_delete_white'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserVisit',
        ),
    ]
