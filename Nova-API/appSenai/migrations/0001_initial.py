# Generated by Django 4.2.5 on 2023-09-25 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('emai', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, unique=True)),
                ('descriçao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120, unique=True)),
                ('descriçao', models.TextField()),
                ('dataEntrega', models.DateField()),
                ('concluida', models.BooleanField(default=False)),
                ('Aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appSenai.aluno')),
                ('Diciplina', models.ManyToManyField(to='appSenai.diciplina')),
            ],
        ),
    ]
