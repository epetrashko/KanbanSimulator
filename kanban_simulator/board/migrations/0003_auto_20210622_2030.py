# Generated by Django 3.1.3 on 2021-06-22 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_userstory'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userstory',
            name='is_expedite',
            field=models.BooleanField(default=False),
        ),
    ]
