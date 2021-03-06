# Generated by Django 3.2.9 on 2022-04-25 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_no', models.CharField(max_length=200)),
                ('create_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('contract_date', models.DateField(null=True)),
                ('customer', models.CharField(max_length=200)),
                ('apply_company', models.CharField(max_length=200)),
                ('service_type', models.CharField(max_length=200)),
                ('service_Package', models.CharField(max_length=200)),
                ('contract_template', models.CharField(blank=True, max_length=200, null=True)),
                ('Payment_Mode', models.CharField(blank=True, max_length=50, null=True)),
                ('untaxed_amount', models.IntegerField()),
                ('tax_amount', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_no', models.CharField(max_length=200)),
                ('CV_Resum', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('Passpost_Scan_Copy', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('Emirates_ID', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('Ntional_ID', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('Additional_Documen', models.ImageField(blank=True, default=None, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Other_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_no', models.CharField(max_length=200)),
                ('salesmen', models.CharField(blank=True, max_length=50, null=True)),
                ('sales_team', models.CharField(blank=True, max_length=50, null=True)),
                ('company', models.CharField(blank=True, max_length=50)),
                ('customer_refrance', models.CharField(blank=True, max_length=50)),
                ('fiscal_position', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_no', models.CharField(max_length=200)),
                ('product', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.IntegerField(blank=True, default=None, null=True)),
                ('qty', models.IntegerField(blank=True, default=None, null=True)),
                ('Untaxed_Amount', models.IntegerField(blank=True, null=True)),
                ('tax', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
