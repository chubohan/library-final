# Generated by Django 4.2.6 on 2023-11-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0022_function_slug1_function1_slug2_function2_slug3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='function',
            old_name='author1',
            new_name='rule',
        ),
        migrations.RemoveField(
            model_name='function',
            name='book',
        ),
        migrations.RemoveField(
            model_name='function',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='function',
            name='time',
        ),
        migrations.RemoveField(
            model_name='function',
            name='type',
        ),
        migrations.AddField(
            model_name='function2',
            name='activitytime',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='function2',
            name='activitycontant',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='function2',
            name='activitynotice',
            field=models.TextField(max_length=200),
        ),
    ]
