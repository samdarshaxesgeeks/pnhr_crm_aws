# Generated by Django 4.0.3 on 2022-04-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0009_alter_customerdetails_parish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdetails',
            name='parish',
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='passport_no',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
