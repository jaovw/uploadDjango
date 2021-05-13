# Generated by Django 3.1.6 on 2021-02-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0003_delete_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('Quantidade', models.IntegerField()),
                ('Descrição', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('apdated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]