# Generated by Django 3.0.7 on 2023-07-17 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0013_tmpitemhelpersession'),
        ('cl_table', '0033_customerextended'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='img')),
                ('item_sitelist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist')),
                ('services', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Stock')),
            ],
            options={
                'db_table': 'Images',
            },
        ),
    ]
