# Generated by Django 3.0.3 on 2020-02-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasta', models.CharField(max_length=100)),
                ('comarca', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
    ]
