# Generated by Django 2.0.6 on 2018-08-13 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_auto_20180813_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default=''),
        ),
    ]