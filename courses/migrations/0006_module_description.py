# Generated by Django 3.2.7 on 2021-09-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_content_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
