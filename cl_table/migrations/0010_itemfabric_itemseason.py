# Generated by Django 3.0.7 on 2023-07-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0009_itemsize_itemsizepack'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemFabric',
            fields=[
                ('itm_id', models.AutoField(primary_key=True, serialize=False)),
                ('itm_code', models.CharField(blank=True, max_length=10, null=True)),
                ('itm_desc', models.CharField(blank=True, max_length=40, null=True)),
                ('itm_status', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Item_Fabric',
            },
        ),
        migrations.CreateModel(
            name='ItemSeason',
            fields=[
                ('season_id', models.AutoField(db_column='Season_ID', primary_key=True, serialize=False)),
                ('season_code', models.CharField(blank=True, db_column='Season_Code', max_length=10, null=True)),
                ('season_desc', models.CharField(blank=True, db_column='Season_Desc', max_length=50, null=True)),
                ('season_shortdesc', models.CharField(blank=True, db_column='Season_ShortDesc', max_length=10, null=True)),
                ('season_user', models.CharField(blank=True, db_column='Season_User', max_length=50, null=True)),
                ('season_date', models.DateTimeField(blank=True, db_column='Season_Date', null=True)),
                ('season_time', models.DateTimeField(blank=True, db_column='Season_Time', null=True)),
                ('season_isactive', models.BooleanField(db_column='Season_Isactive', default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'item_Season',
            },
        ),
    ]
