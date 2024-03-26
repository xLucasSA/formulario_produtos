# Generated by Django 5.0.3 on 2024-03-23 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('valor', models.FloatField()),
                ('disponivel', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')])),
            ],
            options={
                'ordering': ['valor'],
            },
        ),
    ]
