# Generated by Django 3.2.7 on 2021-09-29 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_module_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
