# Generated by Django 3.0.6 on 2020-09-05 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantasapp', '0003_auto_20200818_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='pu',
            field=models.IntegerField(null=True),
        ),
    ]
