# Generated by Django 3.0.5 on 2021-02-05 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isarps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChapterIsarp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=50, verbose_name='Capítulo')),
                ('description', models.CharField(max_length=150, verbose_name='Descripción')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
            ],
            options={
                'verbose_name': 'Capítulo',
                'verbose_name_plural': 'Capítulos',
            },
        ),
        migrations.AddField(
            model_name='isarp',
            name='chapters',
            field=models.ManyToManyField(to='isarps.ChapterIsarp', verbose_name='Capítulo'),
        ),
    ]
