from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from .models import EquipmentType, Equipment
from .serializers import EquipmentSerializer, EquipmentTypeSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .filters import EquipmentTypeFilter, EquipmentFilter
from rest_framework.decorators import api_view


class EquipmenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class EquipmentAPIList(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = EquipmenAPIListPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class  = EquipmentFilter      

    def post(self, request, format=None):
        data = request.data 
        many = isinstance(data, list) 

        # проверяем, передается ли в запросе правильный тип данных для equipment_type_id
        equipment_type = data.get('equipment_type')
        try:
            equipment_type_id = EquipmentType.objects.get(id=equipment_type)
        except EquipmentType.DoesNotExist:
            return Response({'error': 'Invalid equipment type.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = EquipmentSerializer(data=request.data, many=many) 
        if serializer.is_valid(): 
            equipment = serializer.save()
            equipment.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class EquipmentAPIView(APIView):

    def get(self, request,  *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            w = Equipment.objects.all()
            return Response({'posts': EquipmentSerializer(w, many=True).data})
        mymodel = get_object_or_404(Equipment, pk=pk)
        serializer = EquipmentSerializer(mymodel)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Equipment.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = EquipmentSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        return Response({"post": "delete post " + str(pk)})
    


class EquipmentTypeAPIList(generics.ListCreateAPIView):
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = EquipmenAPIListPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class  = EquipmentTypeFilter


    def post(self, request, format=None):
        data = request.data
        many = isinstance(data, list)
        serializer = EquipmentTypeSerializer(data=data, many=many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EquipmentTypeAPIView(APIView):

    def get(self, request,  *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            w = EquipmentType.objects.all()
            return Response({'posts': EquipmentTypeSerializer(w, many=True).data})
        mymodel = get_object_or_404(Equipment, pk=pk)
        serializer = EquipmentTypeSerializer(mymodel)
        return Response(serializer.data)
    
