# Generated by Django 4.2.2 on 2023-07-13 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0004_alter_announcedpuresults_result_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcedpuresults',
            name='result_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lga',
            name='date_entered',
            field=models.DateTimeField(blank=True),
        ),
    ]
