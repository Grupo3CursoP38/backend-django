# Generated by Django 3.2.9 on 2021-11-15 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_example', '0002_auto_20211115_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
