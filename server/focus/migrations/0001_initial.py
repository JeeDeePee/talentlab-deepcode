# Generated by Django 2.0.6 on 2018-07-18 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modules', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.Category')),
            ],
            options={
                'verbose_name': 'Kompetenz',
                'verbose_name_plural': 'Kompetenzen',
            },
        ),
        migrations.CreateModel(
            name='CompetenceEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('current_level', models.PositiveIntegerField(default=0, verbose_name='Kompetenzlevel')),
                ('next_evaluation', models.DateField(blank=True, null=True, verbose_name='Nächste Bewertung')),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='focus.Competence')),
            ],
            options={
                'verbose_name': 'Kompetenz Eintrag',
                'verbose_name_plural': 'Kompetenz Einträge',
            },
        ),
        migrations.CreateModel(
            name='Focus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Fokus',
                'verbose_name_plural': 'Fokus',
            },
        ),
        migrations.AddField(
            model_name='competenceentry',
            name='focus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='focus.Focus'),
        ),
    ]