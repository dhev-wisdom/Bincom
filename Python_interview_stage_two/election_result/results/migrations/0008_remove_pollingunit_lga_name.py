# Generated by Django 4.2.2 on 2023-07-13 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0007_alter_pollingunit_polling_unit_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pollingunit',
            name='lga_name',
        ),
    ]
