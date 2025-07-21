from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Career
from .serializers import CareerSerializer

class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    
    def list(self, request, *args, **kwargs):
        """GET /careers/ - Listar todos os posts"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        """POST /careers/ - Criar novo post"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        career = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        """GET /careers/{id}/ - Buscar post específico"""
        career = get_object_or_404(Career, pk=pk)
        serializer = self.get_serializer(career)
        return Response(serializer.data)
    
    def partial_update(self, request, pk=None):
        """PATCH /careers/{id}/ - Atualizar title e/ou content apenas"""
        career = get_object_or_404(Career, pk=pk)
        
        """ Filtrar apenas campos permitidos para atualização """
        allowed_fields = {'title', 'content'}
        filtered_data = {k: v for k, v in request.data.items() if k in allowed_fields}
        
        serializer = self.get_serializer(career, data=filtered_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        """PUT não é especificado na documentação, redireciona para PATCH"""
        return self.partial_update(request, pk)
    
    def destroy(self, request, pk=None):
        """DELETE /careers/{id}/ - Deletar post"""
        career = get_object_or_404(Career, pk=pk)
        career.delete()
        """ Retorna objeto vazio conforme documentação""" 
        return Response({}, status=status.HTTP_200_OK)