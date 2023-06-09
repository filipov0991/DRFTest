# Generated by Django 4.2 on 2023-05-01 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drfsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Obr',
            new_name='Equipment',
        ),
        migrations.RenameModel(
            old_name='Tip_obr',
            new_name='EquipmentType',
        ),
        migrations.RenameField(
            model_name='equipment',
            old_name='tip',
            new_name='type',
        ),
        migrations.AlterUniqueTogether(
            name='equipment',
            unique_together={('sn', 'type')},
        ),
    ]
