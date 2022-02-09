# Generated by Django 4.0.1 on 2022-02-09 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0005_viralload_vl_captured_alter_viralload_vl_results'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rerand',
            name='rerand_id',
        ),
        migrations.AddField(
            model_name='rerand',
            name='participants_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminpanel.participants'),
        ),
        migrations.AddField(
            model_name='rerand',
            name='viralload_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminpanel.viralload'),
        ),
    ]