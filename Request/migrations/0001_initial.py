# Generated by Django 2.2 on 2020-02-06 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('request', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField()),
            ],
            options={
                'db_table': 'requests',
            },
        ),
    ]