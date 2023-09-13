# Generated by Django 3.0.7 on 2023-07-17 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0059_masterdatastock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skillstaff',
            fields=[
                ('id', models.BigAutoField(db_column='Id', primary_key=True, serialize=False)),
                ('sitecode', models.CharField(blank=True, db_column='siteCode', max_length=10, null=True)),
                ('staffcode', models.CharField(blank=True, db_column='staffCode', max_length=20, null=True)),
                ('itemcode', models.CharField(blank=True, db_column='itemCode', max_length=20, null=True)),
            ],
            options={
                'db_table': 'skillstaff',
            },
        ),
    ]
