# Generated by Django 2.1.7 on 2019-02-28 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pruebas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo1', models.CharField(blank=True, max_length=100, null=True)),
                ('campo2', models.EmailField(max_length=254)),
                ('campo3', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
