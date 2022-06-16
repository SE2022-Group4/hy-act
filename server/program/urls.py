from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.ProgramViewSet)

urlpatterns = [
    path('category/', views.CategoryView.as_view()),
    path('department/', views.DepartmentView.as_view()),
    path('lecturer/', views.LecturerListView.as_view()),
    path('my/', views.MyProgramApplicationListView.as_view()),  # DEPRECATED. Replaced to /api/v1/programs/my/applications/
    path('my/applications/', views.MyProgramApplicationListView.as_view()),
    path('my/managing-programs/', views.MyProgramManagingListView.as_view()),
    path('my/instructing-programs/', views.MyProgramInstructingListView.as_view()),

    # This routing rules should be placed at the end
    path('', include(router.urls)),
    path('<int:pk>/apply/', views.ProgramApplyView.as_view()),
    path('<int:pk>/cancel/', views.ProgramApplicationCancelView.as_view()),
    path('<int:pk>/attendance/', views.ProgramAttendanceStatusView.as_view()),
    path('<int:pk>/attendance/code/create/', views.ProgramAttendanceCodeGenerateView.as_view()),
    path('<int:pk>/attendance/code/verify/', views.ProgramAttendanceCodeVerifyView.as_view()),
]
