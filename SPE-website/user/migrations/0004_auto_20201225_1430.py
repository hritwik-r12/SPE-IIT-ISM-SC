# Generated by Django 3.1.1 on 2020-12-25 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201225_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='SPE_ID',
            field=models.CharField(blank=True, default=0, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='institute_registration_number',
            field=models.CharField(blank=True, default=0, max_length=20, null=True, unique=True),
        ),
    ]
