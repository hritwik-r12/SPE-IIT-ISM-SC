# Generated by Django 3.1.1 on 2020-09-29 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200910_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='google_doc_url',
            field=models.URLField(default='#', max_length=500),
            preserve_default=False,
        ),
    ]