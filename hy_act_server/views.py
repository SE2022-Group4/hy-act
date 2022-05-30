from django import views
from django.http import HttpResponse
from rest_framework import status


class HeartBeatView(views.View):
    """
    Simple heartbeat http view for health check
    """
    def get(self, request):
        return HttpResponse(status=status.HTTP_200_OK)

