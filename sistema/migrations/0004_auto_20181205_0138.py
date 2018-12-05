# Generated by Django 2.1.3 on 2018-12-05 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_listaproducto_oferta'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='fechaFin',
            field=models.DateField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oferta',
            name='fechaInicio',
            field=models.DateField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oferta',
            name='sucursal',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sistema.Sucursal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oferta',
            name='vigente',
            field=models.BooleanField(default=True),
        ),
    ]