# Generated by Django 3.0.7 on 2020-06-16 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnterpriseRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterpriseName', models.CharField(max_length=50, verbose_name='Sirket Adi')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('password', models.CharField(max_length=50, verbose_name='Parol')),
                ('address', models.CharField(max_length=250, verbose_name='Unvan')),
                ('zipp', models.CharField(max_length=50, verbose_name='ZIP')),
                ('tel', models.CharField(max_length=50, verbose_name='Telefon')),
                ('mob', models.CharField(max_length=50, verbose_name='Mob')),
                ('fax', models.CharField(max_length=50, verbose_name='Fax')),
                ('wep', models.CharField(max_length=50, verbose_name='Wep')),
                ('rejim', models.CharField(max_length=50, verbose_name='Rejim')),
                ('leader', models.CharField(max_length=50, verbose_name='Rehber')),
            ],
        ),
    ]