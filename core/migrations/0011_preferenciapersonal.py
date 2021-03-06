# Generated by Django 3.2.13 on 2022-05-05 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_categoriapreferenciapersonal'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreferenciaPersonal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombrepreferenciapersonal', models.CharField(max_length=30, null=True, unique=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('idcategoriapreferenciapersonal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoriapreferenciapersonal')),
            ],
            options={
                'verbose_name': ' Preferencia Personal',
                'verbose_name_plural': 'Preferencia Personal',
            },
        ),
    ]
