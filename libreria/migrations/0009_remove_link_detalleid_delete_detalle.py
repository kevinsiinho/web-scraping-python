# Generated by Django 4.2.3 on 2023-07-15 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0008_comentarios_detalle_tipo_alter_frase_table_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='detalleid',
        ),
        migrations.DeleteModel(
            name='Detalle',
        ),
    ]