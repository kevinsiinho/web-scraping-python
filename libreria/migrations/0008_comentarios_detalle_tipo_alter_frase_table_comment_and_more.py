# Generated by Django 4.2.3 on 2023-07-15 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0007_alter_frase_options_alter_link_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.TextField(max_length=200, null=True)),
                ('date', models.DateField(null=True, verbose_name='Fecha')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45, null=True, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45, null=True, verbose_name='nombre')),
            ],
        ),
        migrations.AlterModelTableComment(
            name='frase',
            table_comment=None,
        ),
        migrations.AddField(
            model_name='frase',
            name='idlink',
            field=models.ForeignKey(db_column='idlink', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='libreria.link'),
        ),
        migrations.AddField(
            model_name='frase',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='frase',
            name='texto',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='link',
            name='clase',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='link',
            name='estado',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='link',
            name='url',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='frase',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='link',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='frase',
            table=None,
        ),
        migrations.AlterModelTable(
            name='link',
            table=None,
        ),
        migrations.AddField(
            model_name='link',
            name='detalleid',
            field=models.ForeignKey(db_column='detalleid', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='libreria.detalle'),
        ),
        migrations.AddField(
            model_name='link',
            name='tipoid',
            field=models.ForeignKey(db_column='tipoid', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='libreria.tipo'),
        ),
    ]