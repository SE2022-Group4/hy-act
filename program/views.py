from rest_framework import viewsets, permissions

from program.models import Program
from program.serializers import ProgramSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.order_by('-created_at')
    serializer_class = ProgramSerializer
    permission_classes = [permissions.IsAuthenticated]
