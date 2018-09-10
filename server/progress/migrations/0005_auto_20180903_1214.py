# Generated by Django 2.0.6 on 2018-09-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0004_auto_20180820_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermoduleprogress',
            name='commitment_support_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usermoduleprogress',
            name='impact_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usermoduleprogress',
            name='measurement_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usermoduleprogress',
            name='measures_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usermoduleprogress',
            name='resources_skills_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usermoduleprogress',
            name='time_frame_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]