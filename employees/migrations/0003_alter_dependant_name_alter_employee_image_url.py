# Generated by Django 4.0.3 on 2022-03-28 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20210923_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependant',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image_url',
            field=models.ImageField(upload_to=''),
        ),
    ]
