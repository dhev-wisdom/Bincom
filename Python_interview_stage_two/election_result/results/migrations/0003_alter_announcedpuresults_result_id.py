# Generated by Django 4.2.2 on 2023-07-13 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_alter_agentname_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcedpuresults',
            name='result_id',
            field=models.AutoField(default=111, primary_key=True, serialize=False),
        ),
    ]
