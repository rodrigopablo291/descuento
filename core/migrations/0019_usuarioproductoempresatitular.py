# Generated by Django 3.2.13 on 2022-05-05 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_preferenciapersonal'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioProductoEmpresaTitular',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idproductoempresatitular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.productoempresatitular')),
                ('idusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
            options={
                'verbose_name': 'Usuario Producto Empresa Titular',
                'verbose_name_plural': 'Usuario Producto Empresa Titular',
            },
        ),
    ]
