# Generated by Django 3.2.7 on 2021-09-29 05:37

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20210912_1138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
