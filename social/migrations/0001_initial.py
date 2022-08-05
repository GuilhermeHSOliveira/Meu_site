# Generated by Django 4.0.3 on 2022-03-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chave', models.SlugField(max_length=100, unique=True, verbose_name='Identificação Rede')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('url', models.URLField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('altered', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
