from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'programs', views.ProgramViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
