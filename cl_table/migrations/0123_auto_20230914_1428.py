# Generated by Django 3.0.7 on 2023-09-14 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0122_auto_20230914_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fmspw',
            name='flgtransacdisc',
            field=models.BooleanField(db_column='flgtransacdisc', default=False, null=True),
        ),
    ]
