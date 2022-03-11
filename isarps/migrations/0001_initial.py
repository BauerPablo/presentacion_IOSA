# Generated by Django 3.0.5 on 2021-02-05 17:35

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Isarp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_isarp', models.CharField(max_length=50, verbose_name='Título ISARP')),
                ('content_isarp', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Contenido ISARP')),
                ('slug_isarp', models.CharField(max_length=150, verbose_name='slug ISARP')),
                ('order_isarp', models.IntegerField(default=0, verbose_name='Orden')),
                ('public_isarp', models.BooleanField(verbose_name='Público')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'ISARP',
                'verbose_name_plural': "ISARP's",
            },
        ),
    ]
