# Generated by Django 4.1.6 on 2023-03-02 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0003_house_delete_houseprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='zipcode',
            field=models.IntegerField(max_length=10),
        ),
    ]
