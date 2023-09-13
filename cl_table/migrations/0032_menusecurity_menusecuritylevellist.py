# Generated by Django 3.0.7 on 2023-07-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0031_securitycontrollist_securitylevellist'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuSecurity',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('security_level_code', models.CharField(blank=True, db_column='SECURITY_LEVEL_CODE', max_length=20, null=True)),
                ('security_level_desc', models.CharField(blank=True, db_column='SECURITY_LEVEL_DESC', max_length=50, null=True)),
                ('is_active', models.BooleanField(db_column='IS_ACTIVE')),
            ],
            options={
                'db_table': 'Menu_Security',
            },
        ),
        migrations.CreateModel(
            name='MenuSecuritylevellist',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('security_level_code', models.CharField(blank=True, db_column='SECURITY_LEVEL_CODE', max_length=20, null=True)),
                ('menu_list', models.CharField(blank=True, db_column='MENU_LIST', max_length=100, null=True)),
                ('menu_active', models.BooleanField(db_column='MENU_ACTIVE')),
            ],
            options={
                'db_table': 'Menu_SecurityLevelList',
            },
        ),
    ]