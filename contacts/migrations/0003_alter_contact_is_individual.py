# Generated by Django 4.0.3 on 2022-04-01 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contact_is_individual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='is_individual',
            field=models.CharField(blank=True, choices=[('company', 'company'), ('indivisual', 'indivisual')], max_length=20, null=True),
        ),
    ]
