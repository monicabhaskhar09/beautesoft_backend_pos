# Generated by Django 3.0.7 on 2023-07-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0013_tmpitemhelpersession'),
        ('cl_table', '0106_studiowork'),
    ]

    operations = [
        migrations.CreateModel(
            name='MGMPolicyCloud',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('level', models.IntegerField(db_column='level', null=True)),
                ('point_value', models.FloatField(blank=True, db_column='Point_Value', null=True)),
                ('isactive', models.BooleanField(db_column='IsActive', default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('minimum_purchase_amt', models.FloatField(blank=True, null=True)),
                ('no_of_reward_times', models.IntegerField(blank=True, db_column='no_of_reward_times', null=True)),
                ('site_ids', models.ManyToManyField(blank=True, to='cl_app.ItemSitelist')),
            ],
            options={
                'db_table': 'MGMPolicyCloud',
            },
        ),
    ]
