# Generated by Django 3.0.7 on 2023-07-17 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0023_currencytable'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotationmodel',
            name='currency_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.Currencytable'),
        ),
    ]