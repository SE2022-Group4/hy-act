from django import views
from django.http import Http404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from program.models import Program
from program.serializers import ProgramSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.order_by('-created_at')
    serializer_class = ProgramSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProgramApplyView(APIView):
    def get_object(self, pk):
        try:
            return Program.objects.get(pk=pk)
        except Program.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        program = self.get_object(pk)
        program.apply(request.user)

        return Response(status=status.HTTP_200_OK)
