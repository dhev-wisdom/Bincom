# Generated by Django 4.2.2 on 2023-07-13 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_alter_announcedpuresults_result_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcedpuresults',
            name='result_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
