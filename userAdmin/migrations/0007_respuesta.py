# Generated by Django 3.2.5 on 2023-02-17 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAdmin', '0006_alter_comentario_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('respuesta', models.TextField()),
                ('comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAdmin.comentario')),
            ],
        ),
    ]
