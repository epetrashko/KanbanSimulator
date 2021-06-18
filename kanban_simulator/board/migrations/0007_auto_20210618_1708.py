# Generated by Django 3.1.3 on 2021-06-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_character'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='creator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='started',
            field=models.BooleanField(default=False),
        ),
    ]
