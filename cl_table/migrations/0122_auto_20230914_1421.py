# Generated by Django 3.0.7 on 2023-09-14 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0121_auto_20230914_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fmspw',
            name='is_paymentdate',
            field=models.BooleanField(db_column='PaymentDate', default=False, null=True),
        ),
    ]
