# Generated by Django 4.1.5 on 2023-01-14 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContratacaoPlano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aporte', models.FloatField()),
                ('dataDaContratacao', models.DateTimeField()),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.cliente')),
                ('idProduto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.produto')),
            ],
        ),
    ]