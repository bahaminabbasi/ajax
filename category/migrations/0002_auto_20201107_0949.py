# Generated by Django 3.0.9 on 2020-11-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='nesting_level',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
