# Generated by Django 2.2.4 on 2019-08-06 13:55

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_entry_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
