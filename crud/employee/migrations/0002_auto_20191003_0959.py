# Generated by Django 2.2.4 on 2019-10-03 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='econtact',
            field=models.IntegerField(),
        ),
    ]
