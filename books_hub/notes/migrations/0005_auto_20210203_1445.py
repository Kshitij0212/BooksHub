# Generated by Django 3.1.5 on 2021-02-03 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20210202_1944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'ordering': ('year',), 'verbose_name': 'Notes', 'verbose_name_plural': 'Notes'},
        ),
    ]