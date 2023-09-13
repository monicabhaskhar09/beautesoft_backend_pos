# Generated by Django 3.0.7 on 2023-07-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpLevel',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('level_code', models.CharField(blank=True, db_column='Level_Code', max_length=20, null=True)),
                ('level_desc', models.CharField(blank=True, db_column='Level_Desc', max_length=50, null=True)),
                ('level_isactive', models.BooleanField(db_column='Level_IsActive', default=True)),
                ('level_sequence', models.IntegerField(blank=True, db_column='Level_sequence', null=True)),
                ('level_spa', models.BooleanField(db_column='Level_SPA', null=True)),
                ('mintarget', models.FloatField(blank=True, db_column='MinTarget', null=True)),
                ('fromsalary', models.FloatField(blank=True, db_column='FromSalary', null=True)),
                ('tosalary', models.FloatField(blank=True, db_column='ToSalary', null=True)),
                ('getgroupcomm', models.BooleanField(blank=True, db_column='GetGroupComm', null=True)),
                ('group_code', models.CharField(blank=True, db_column='Group_Code', max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'Emp_Level',
            },
        ),
    ]