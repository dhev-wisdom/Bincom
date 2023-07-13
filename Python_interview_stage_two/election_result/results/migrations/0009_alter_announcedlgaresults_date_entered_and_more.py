# Generated by Django 4.2.2 on 2023-07-13 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0008_remove_pollingunit_lga_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcedlgaresults',
            name='date_entered',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='announcedpuresults',
            name='date_entered',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='announcedstateresults',
            name='date_entered',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='announcedwardresults',
            name='date_entered',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lga',
            name='date_entered',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pollingunit',
            name='date_entered',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ward',
            name='date_entered',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
