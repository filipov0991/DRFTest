# Generated by Django 4.2 on 2023-05-01 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drfsite', '0003_rename_type_equipment_equipment_type_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='equipment_type_id',
            new_name='equipment_type',
        ),
        migrations.AlterUniqueTogether(
            name='equipment',
            unique_together={('serial_number', 'equipment_type')},
        ),
    ]
