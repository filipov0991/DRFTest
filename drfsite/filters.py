import django_filters
from .models import EquipmentType, Equipment


class EquipmentTypeFilter(django_filters.FilterSet):
    class Meta:
        model = EquipmentType
        fields = '__all__'


class EquipmentFilter(django_filters.FilterSet):
    class Meta:
        model = Equipment
        fields = '__all__'
