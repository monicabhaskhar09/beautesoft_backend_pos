# Generated by Django 3.0.7 on 2023-09-26 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0136_auto_20230919_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='passcode',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
