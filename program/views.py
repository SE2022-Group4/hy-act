from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.filters import SearchFilter
from django.http import Http404
from rest_framework import viewsets, permissions, status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from hy_act_server.fields import TimestampField
from program.models import Category, Program, Department, AttendanceCode
from program.serializers import CategorySerializer, ProgramSerializer, DepartmentSerializer


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


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        categories_serialized = CategorySerializer(categories, many=True)
        return Response(categories_serialized.data)

    @extend_schema(
        request=CategorySerializer,
        responses=CategorySerializer,
        # more customizations
    )
    def post(self, request):
        category = CategorySerializer(data=request.data)
        if category.is_valid():
            category.save()
            return Response(category.data, status=status.HTTP_201_CREATED)
        return Response(category.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        departments_serialized = DepartmentSerializer(departments, many=True)
        return Response(departments_serialized.data)

    @extend_schema(
        request=DepartmentSerializer,
        responses=DepartmentSerializer,
        # more customizations
    )
    def post(self, request):
        department = DepartmentSerializer(data=request.data)
        if department.is_valid():
            department.save()
            return Response(department.data, status=status.HTTP_201_CREATED)
        return Response(department.errors, status=status.HTTP_400_BAD_REQUEST)


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


# TODO: Implement Program Attendance Status View
class ProgramAttendanceStatusView(APIView):
    def get(self, request, *args, **kwargs):
        pass


class ProgramAttendanceCodeGenerateView(APIView):
    class RequestDataSerializer(serializers.Serializer):
        # FIXME: Improve comment on choice field
        type = serializers.ChoiceField(help_text="0:프로그램 시작 코드 / 1:프로그램 종료 코드", choices=AttendanceCode.CodeType.choices)

    class ResponseBodySerializer(serializers.Serializer):
        created_at = TimestampField()
        type = serializers.ChoiceField(help_text="0:프로그램 시작 코드 / 1:프로그램 종료 코드", choices=AttendanceCode.CodeType.choices)
        code = serializers.CharField()

    @extend_schema(
        request=RequestDataSerializer,
        responses={
            status.HTTP_200_OK: ResponseBodySerializer,
        }
    )
    def post(self, request, pk, *args, **kwargs):
        if not Program.objects.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        program = Program.objects.get(id=pk)

        serializer = self.RequestDataSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        code_type = serializer.validated_data.get('type')
        attendance_code = program.create_attendance_code(code_type)

        response_body = self.ResponseBodySerializer(attendance_code).data
        return Response(response_body, status=status.HTTP_200_OK)


# TODO: Implement Program Attendance Verify View
class ProgramAttendanceCodeVerifyView(APIView):
    def post(self, request, *args, **kwargs):
        pass
