# Generated by Django 3.0.7 on 2021-07-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20210626_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='version',
            field=models.IntegerField(default=0),
        ),
    ]