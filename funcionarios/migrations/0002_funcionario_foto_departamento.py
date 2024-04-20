# Generated by Django 5.0.4 on 2024-04-19 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='funcionarios/'),
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('funcionarios', models.ManyToManyField(to='funcionarios.funcionario')),
            ],
        ),
    ]