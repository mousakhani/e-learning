# Generated by Django 3.2.7 on 2021-09-29 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_module_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(null=True),
        ),
    ]