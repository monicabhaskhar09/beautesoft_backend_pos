# Generated by Django 3.0.7 on 2023-07-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0063_salarysubtypelookup'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModeOfPayment',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('modename', models.CharField(max_length=40)),
                ('accountcode', models.CharField(max_length=10)),
                ('isactive', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'modeofpayment',
            },
        ),
    ]