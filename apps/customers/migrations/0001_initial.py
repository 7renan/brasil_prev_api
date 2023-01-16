# Generated by Django 4.1.5 on 2023-01-14 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=50)),
                ('dataDeNascimento', models.DateTimeField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=10)),
                ('rendaMensal', models.IntegerField()),
            ],
        ),
    ]
