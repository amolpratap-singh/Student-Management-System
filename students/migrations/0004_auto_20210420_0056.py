# Generated by Django 2.2.8 on 2021-04-19 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20210420_0053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentinfo',
            options={'permissions': (('can_delete_student_info', 'Set student been delete'),)},
        ),
    ]