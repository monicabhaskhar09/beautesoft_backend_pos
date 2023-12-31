# Generated by Django 3.0.7 on 2023-07-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0086_customerformcontrol'),
    ]

    operations = [
        migrations.CreateModel(
            name='MrRewardItemType',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('itemtype_code', models.CharField(db_column='ITEMTYPE_CODE', max_length=20)),
                ('itemtype_desc', models.CharField(blank=True, db_column='ITEMTYPE_DESC', max_length=50, null=True)),
                ('isactive', models.BooleanField(db_column='ISACTIVE')),
            ],
            options={
                'db_table': 'MR_Reward_Item_Type',
            },
        ),
    ]
