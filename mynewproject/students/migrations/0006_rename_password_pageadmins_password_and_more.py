# Generated by Django 4.2.1 on 2023-05-23 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_pageadmins'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pageadmins',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='pageadmins',
            old_name='Username',
            new_name='username',
        ),
    ]
