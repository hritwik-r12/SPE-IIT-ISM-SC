# Generated by Django 3.1.1 on 2020-10-02 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20201002_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registeration',
            old_name='first_user',
            new_name='Member_1',
        ),
        migrations.RenameField(
            model_name='registeration',
            old_name='user2',
            new_name='Member_2',
        ),
        migrations.RenameField(
            model_name='registeration',
            old_name='user3',
            new_name='Member_3',
        ),
        migrations.RenameField(
            model_name='registeration',
            old_name='user4',
            new_name='Member_4',
        ),
        migrations.RenameField(
            model_name='registeration',
            old_name='phone',
            new_name='Mobile_number',
        ),
    ]
