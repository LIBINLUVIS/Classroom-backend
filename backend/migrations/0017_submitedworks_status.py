# Generated by Django 3.1.3 on 2021-05-28 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_auto_20210528_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitedworks',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
