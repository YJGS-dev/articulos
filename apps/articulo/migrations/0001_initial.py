# Generated by Django 4.1.3 on 2022-12-05 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
        ('familia', '0001_initial'),
        ('clase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.SmallIntegerField()),
                ('nombre', models.CharField(max_length=15)),
                ('marca', models.CharField(max_length=15)),
                ('modelo', models.CharField(max_length=20)),
                ('fecha_alta', models.DateField(auto_now_add=True)),
                ('fecha_baja', models.DateField(default='1900-01-01')),
                ('stock', models.SmallIntegerField()),
                ('cantidad', models.SmallIntegerField()),
                ('descontinuado', models.SmallIntegerField(choices=[(1, 'Activado'), (0, 'Desactivado')], default=0)),
                ('estatus', models.SmallIntegerField(choices=[(1, 'Activo'), (0, 'Inactivo')], default=1)),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clase.clase')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='familia.familia')),
            ],
            options={
                'db_table': 'articulo',
            },
        ),
    ]
