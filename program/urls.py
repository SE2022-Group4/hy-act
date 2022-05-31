from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.ProgramViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/apply/', views.ProgramApplyView.as_view()),
    path('category/', views.CategoryView.as_view()),
    path('department/', views.DepartmentView.as_view()),
]
