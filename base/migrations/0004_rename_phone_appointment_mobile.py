# Generated by Django 5.0.3 on 2024-03-05 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_appointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='phone',
            new_name='mobile',
        ),
    ]
