# Generated by Django 3.2 on 2023-01-30 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='created_date',
            new_name='create_date',
        ),
    ]
