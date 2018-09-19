# Generated by Django 2.0.6 on 2018-09-19 18:42

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompetenceEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('current_level', models.PositiveIntegerField(default=0, verbose_name='Kompetenzlevel')),
                ('next_evaluation', models.DateField(blank=True, null=True, verbose_name='Nächste Bewertung')),
            ],
            options={
                'verbose_name': 'Kompetenzeintrag',
                'verbose_name_plural': 'Kompetenzeinträge',
            },
        ),
        migrations.CreateModel(
            name='Focus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Fokus',
                'verbose_name_plural': 'Fokus',
            },
        ),
    ]
