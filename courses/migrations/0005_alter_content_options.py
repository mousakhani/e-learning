# Generated by Django 3.2.7 on 2021-09-29 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20210929_0907'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
    ]
