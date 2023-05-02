from django.db import models
import re
from django.forms import ValidationError


class EquipmentType(models.Model):
    name = models.CharField(max_length=255)
    mask = models.CharField(max_length=100)


class Equipment(models.Model):
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=255, unique=True)
    note = models.CharField(max_length=255)

    class Meta:
        unique_together = ('serial_number', 'equipment_type')
