# Generated by Django 3.0.7 on 2021-07-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20210709_0055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userstory',
            options={'verbose_name_plural': 'User Stories'},
        ),
        migrations.AlterField(
            model_name='team',
            name='wip_limit1',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='team',
            name='wip_limit2',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='team',
            name='wip_limit3',
            field=models.IntegerField(default=4),
        ),
    ]
