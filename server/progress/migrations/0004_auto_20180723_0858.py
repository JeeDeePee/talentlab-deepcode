# Generated by Django 2.0.6 on 2018-07-23 08:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modules', '0001_initial'),
        ('progress', '0003_auto_20180718_1936'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserModule',
            new_name='UserModuleProgress',
        ),
        migrations.RenameModel(
            old_name='UserUnit',
            new_name='UserUnitProgress',
        ),
        migrations.AlterModelOptions(
            name='usermoduleprogress',
            options={'verbose_name': 'UserModuleProgress', 'verbose_name_plural': 'UserModules'},
        ),
        migrations.AlterModelOptions(
            name='userunitprogress',
            options={'verbose_name': 'UserUnitProgress', 'verbose_name_plural': 'UserUnits'},
        ),
    ]
