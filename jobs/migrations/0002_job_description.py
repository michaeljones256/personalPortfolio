# Generated by Django 3.0.4 on 2020-03-25 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.CharField(default='defualt', max_length=1000),
        ),
    ]
