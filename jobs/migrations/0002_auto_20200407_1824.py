# Generated by Django 3.0.5 on 2020-04-07 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='image',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='summary',
            new_name='Summary',
        ),
    ]
