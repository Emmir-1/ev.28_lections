# Generated by Django 4.2.2 on 2023-06-09 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=75, unique=True),
        ),
    ]
