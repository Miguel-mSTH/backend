# Generated by Django 4.0.1 on 2022-01-26 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=200)),
                ('serie', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('procesador', models.CharField(max_length=200)),
                ('memoria', models.IntegerField()),
                ('disco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
