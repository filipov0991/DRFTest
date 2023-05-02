from rest_framework import serializers
from .models import Equipment, EquipmentType
from .validators import validate_serial_number

class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = '__all__'


class EquipmentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipmentType
        fields = '__all__'

   
