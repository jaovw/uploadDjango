# Generated by Django 3.1.6 on 2021-04-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0008_produto1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='Ramo',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='Quantidade',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
