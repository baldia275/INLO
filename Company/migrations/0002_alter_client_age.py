# Generated by Django 4.1.5 on 2023-01-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='age',
            field=models.IntegerField(),
        ),
    ]