# Generated by Django 4.0.1 on 2022-02-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0004_alter_viralload_vl_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='viralload',
            name='vl_captured',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='viralload',
            name='vl_results',
            field=models.IntegerField(),
        ),
    ]
