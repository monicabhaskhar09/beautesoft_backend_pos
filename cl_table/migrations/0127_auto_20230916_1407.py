# Generated by Django 3.0.7 on 2023-09-16 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0126_auto_20230915_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemsetup',
            name='isactive',
            field=models.BooleanField(default=True, null=True),
        ),
    ]