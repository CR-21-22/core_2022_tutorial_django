# Generated by Django 4.0.1 on 2022-10-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0003_coordenador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='prioridade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
