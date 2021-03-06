# Generated by Django 4.0.3 on 2022-04-18 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm_app', '0008_alter_add_more_detail_id_alter_allowance_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(max_length=200)),
                ('invoice_date', models.DateField(null=True)),
                ('s_name', models.CharField(max_length=200)),
                ('s_email', models.EmailField(max_length=254, null=True)),
                ('s_state', models.CharField(max_length=200)),
                ('s_address', models.CharField(max_length=200)),
                ('b_name', models.CharField(max_length=200)),
                ('b_email', models.EmailField(max_length=254, null=True)),
                ('b_state', models.CharField(max_length=200)),
                ('b_address', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('sub_total', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('tax_amount', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('grand_total', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('amount_deposit', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('amount_due', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.IntegerField(blank=True, default=None, null=True)),
                ('qty', models.IntegerField(blank=True, default=None, null=True)),
                ('tax', models.IntegerField(blank=True, default=None, null=True)),
                ('total', models.IntegerField(blank=True, default=None, null=True)),
                ('invoice_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice1.invoice')),
            ],
        ),
    ]
