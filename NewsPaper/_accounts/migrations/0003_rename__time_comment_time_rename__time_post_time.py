# Generated by Django 4.1.4 on 2022-12-14 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_accounts', '0002_category_post_postcategory_post_categories_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='_time',
            new_name='time',
        ),
    ]