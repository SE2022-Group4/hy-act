from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter

from program.models import Program
from program.serializers import ProgramSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.order_by('-created_at')
    serializer_class = ProgramSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
    filterset_fields = {
        'category': ['exact'],
        'sex': ['exact'],
        'department': ['exact'],
        'program_start_at': ['gte'],
        'program_end_at': ['lte'],
    }
    permission_classes = [permissions.IsAuthenticated]
