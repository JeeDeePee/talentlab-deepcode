# Generated by Django 2.0.6 on 2018-09-10 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0006_usermoduleprogress_learnings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermoduleprogress',
            old_name='learnings',
            new_name='learnings_text',
        ),
    ]