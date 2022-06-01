from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.ProgramViewSet)

urlpatterns = [
    path('category/', views.CategoryView.as_view()),
    path('department/', views.DepartmentView.as_view()),

    # This routing rules should be placed at the end
    path('', include(router.urls)),
    path('<int:pk>/apply/', views.ProgramApplyView.as_view()),
]
