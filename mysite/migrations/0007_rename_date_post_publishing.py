# Generated by Django 4.2.6 on 2023-10-29 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_rename_now_post_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='publishing',
        ),
    ]