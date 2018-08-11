# Generated by Django 2.0 on 2018-08-08 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceptoresGrupo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_r', models.CharField(default='', max_length=10)),
                ('tipo_mensaje', models.CharField(max_length=10)),
                ('mensaje', models.CharField(max_length=500)),
                ('estado_mensaje', models.CharField(max_length=10)),
                ('id_chat_grupo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Main.ChatsGrupos')),
                ('id_g', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.GrupoChat')),
            ],
            options={
                'verbose_name': 'Receptores Grupo',
                'verbose_name_plural': 'Receptores Grupos',
                'ordering': ['id'],
            },
        ),
        migrations.RenameField(
            model_name='participantesgrupo',
            old_name='id_r',
            new_name='id_usuario',
        ),
        migrations.RemoveField(
            model_name='participantesgrupo',
            name='estado_mensaje',
        ),
        migrations.RemoveField(
            model_name='participantesgrupo',
            name='id_chat_grupo',
        ),
        migrations.RemoveField(
            model_name='participantesgrupo',
            name='mensaje',
        ),
        migrations.RemoveField(
            model_name='participantesgrupo',
            name='tipo_mensaje',
        ),
        migrations.AlterField(
            model_name='participantesgrupo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
