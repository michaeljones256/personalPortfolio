# Generated by Django 3.0.4 on 2020-03-25 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.CharField(max_length=200)),
                ('description', models.CharField(default='defualt', max_length=1000)),
                ('glink', models.CharField(default='defualt', max_length=200)),
            ],
        ),
    ]
