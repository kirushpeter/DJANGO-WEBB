# Generated by Django 3.0.5 on 2020-04-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('typee', models.CharField(max_length=100)),
            ],
        ),
    ]
