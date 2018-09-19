# Generated by Django 2.0.6 on 2018-09-19 13:42

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0021_image_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('teaser', models.TextField(default='')),
                ('icon_component', models.CharField(default='EmptyIcon', max_length=100)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Kategorie',
                'verbose_name_plural': 'Kategorien',
            },
            bases=('wagtailcore.page',),
        ),
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
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(blank=True, default=0, help_text='Ziel-Level', null=True)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Ziel',
                'verbose_name_plural': 'Ziele',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('skill', models.CharField(help_text="e.g. 'Leadership'", max_length=255)),
                ('teaser', models.TextField()),
                ('lead', models.TextField()),
                ('description', wagtail.core.fields.RichTextField()),
                ('video_id', models.PositiveIntegerField(blank=True, help_text='Vimeo video id (https://vimeo.com/<this-id>)', null=True)),
                ('video_description', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('video_thumbnail_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('resources', wagtail.core.fields.StreamField([('link', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock()), ('description', wagtail.core.blocks.CharBlock())], icon='link')), ('document', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock()), ('description', wagtail.core.blocks.CharBlock())], icon='doc-empty'))], blank=True, null=True)),
                ('resources_normalized', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='helper field for graphql api', null=True)),
                ('tools', wagtail.core.fields.StreamField([('link', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock()), ('description', wagtail.core.blocks.CharBlock())], icon='link')), ('document', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock()), ('description', wagtail.core.blocks.CharBlock())], icon='doc-empty'))], blank=True, null=True)),
                ('tools_normalized', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='helper field for graphql api', null=True)),
                ('hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Lernmodul',
                'verbose_name_plural': 'Lernmodule',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('teaser', models.TextField(default='')),
                ('lead', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('objectives', wagtail.core.fields.RichTextField()),
                ('content', wagtail.core.fields.RichTextField()),
                ('teacher', wagtail.core.fields.RichTextField()),
                ('requirements', wagtail.core.fields.RichTextField()),
                ('type', models.CharField(choices=[('webinar', 'Webinar'), ('kurs', 'Kurs'), ('hybrid', 'Hybrid'), ('coaching', 'Coaching'), ('tinder', 'Tinder'), ('lernfilm', 'Lernfilm'), ('webex', 'Webex')], max_length=100)),
                ('count', models.CharField(help_text="e.g. '3 Veranstaltungen'", max_length=255)),
                ('duration', models.CharField(help_text="e.g. 'je 2 Tage'", max_length=255)),
                ('price', models.CharField(default='', help_text="e.g. 'CHF 150'", max_length=255)),
                ('competences', models.ManyToManyField(to='modules.Competence')),
            ],
            options={
                'verbose_name': 'Lernangebot',
                'verbose_name_plural': 'Lernangebote',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='goal',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modules.Module'),
        ),
    ]
