# Generated by Django 4.0.3 on 2022-04-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice1', '0002_remove_invoice_customer_alter_invoice_b_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='b_name',
            field=models.CharField(max_length=200),
        ),
    ]
