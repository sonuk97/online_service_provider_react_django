# Generated by Django 4.2.7 on 2024-06-06 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_customuser_address_customuser_agency_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='department',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
