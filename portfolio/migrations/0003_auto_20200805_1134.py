# Generated by Django 2.1.1 on 2020-08-05 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200805_1129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='title1',
            new_name='title',
        ),
    ]
