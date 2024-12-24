# Generated by Django 5.1.4 on 2024-12-24 22:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Referencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='referencias')),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(choices=[('D', 'Design'), ('EV', 'Edição de Vídeo')], default='D', max_length=2)),
                ('prazo_entrega', models.DateTimeField()),
                ('preco', models.FloatField()),
                ('reservado', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('C', 'Em criação'), ('AA', 'Aguardando aprovação'), ('F', 'Finalizado')], default='C', max_length=2)),
                ('arquivo_final', models.FileField(blank=True, null=True, upload_to='')),
                ('profissional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('referencias', models.ManyToManyField(to='jobs.referencias')),
            ],
        ),
    ]
