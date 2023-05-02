from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework import serializers
from .models import Equipment
from .validators import validate_serial_number


@receiver(pre_save, sender=Equipment)
def validate_equipment_serial_number(sender, instance, **kwargs):
    if not validate_serial_number(instance.serial_number, instance.equipment_type.id):
        raise serializers.ValidationError("Invalid serial number!!!")