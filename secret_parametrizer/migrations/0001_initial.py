# Generated by Django 2.2.14 on 2020-08-01 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SecretParametrizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Name')),
                ('code', models.CharField(blank=True, max_length=64, null=True, verbose_name='Code')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('url_to_call', models.TextField(blank=True, null=True, verbose_name='URL')),
                ('token', models.TextField(blank=True, null=True, verbose_name='TOKEN')),
                ('key', models.CharField(blank=True, max_length=64, null=True, verbose_name='Key')),
            ],
        ),
    ]
