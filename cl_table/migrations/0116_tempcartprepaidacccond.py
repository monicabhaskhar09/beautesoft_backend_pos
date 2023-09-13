# Generated by Django 3.0.7 on 2023-09-04 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0071_posdiscquant'),
        ('cl_table', '0115_tempprepaidaccountcondition'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempcartprepaidAccCond',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('cart_id', models.CharField(max_length=20, null=True)),
                ('use_amt', models.FloatField(blank=True, db_column='Use_Amt', null=True)),
                ('bal_amt', models.FloatField(blank=True, db_column='Bal_Amt', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('itemcart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.ItemCart')),
                ('prepaidaccount_cond', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.PrepaidAccountCondition')),
            ],
            options={
                'db_table': 'TempCartPrepaid_Account_Condition',
            },
        ),
    ]