# Generated by Django 5.0.3 on 2024-11-06 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_category_tag_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
