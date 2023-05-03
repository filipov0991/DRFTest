from .models import EquipmentType
from rest_framework import serializers

def validate_serial_number(serial_number, equipment_type_id):
    equipment_type = EquipmentType.objects.get(pk=equipment_type_id)
    mask = equipment_type.mask
    if len(serial_number) != len(mask):
        raise serializers.ValidationError('Длина серийного номера не соответствует маске')
    for i, char in enumerate(mask):
        print(char, serial_number[i])
        if char == 'N' and not serial_number[i].isdigit():
            raise serializers.ValidationError('Символ {} в позиции {} не является цифрой'.format(serial_number[i], i))
        elif char == "A" and not serial_number[i].isalpha() and not serial_number[i].isupper():
            raise serializers.ValidationError('Символ {} в позиции {} не является буквой'.format(serial_number[i], i))
        elif char == "a" and not serial_number[i].isalpha() and not serial_number[i].islower():
            raise serializers.ValidationError('Символ {} в позиции {} не является буквой'.format(serial_number[i], i))
        elif char == "X" and not (serial_number[i].isalpha() and serial_number[i].isupper()) and not serial_number[i].isdigit():
            raise serializers.ValidationError('Символ {} в позиции {} не является буквой или цифрой'.format(serial_number[i], i))
        elif char == 'Z' and serial_number[i] not in ['-', '_', '@']:
            raise serializers.ValidationError('Символ {} в позиции {} не является допустимым символом'.format(serial_number[i], i))
    return True