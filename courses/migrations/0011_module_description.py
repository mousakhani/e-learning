# Generated by Django 3.2.7 on 2021-09-29 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20210929_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]