import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.filters import SearchFilter
from django.http import Http404
from rest_framework import viewsets, permissions, status, serializers, filters
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from hy_act_server.fields import TimestampField
from program.models import Category, Program, Department, AttendanceCode, Application
from program.serializers import CategorySerializer, ProgramSerializer, DepartmentSerializer, ProgramDetailSerializer
from user.serializers import UserSerializer

User = get_user_model()


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

        if Application.objects.filter(program=program, student=request.user).exists():
            response_data = {
                "error_code": 10003,
                "error_msg": "Application data for program already exists"
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        program.apply(request.user)

        return Response(status=status.HTTP_200_OK)


class ProgramAttendanceStatusView(APIView):
    @extend_schema(
        responses={
            status.HTTP_200_OK: ProgramDetailSerializer,
        }
    )
    def get(self, request, pk, *args, **kwargs):
        program = Program.objects.prefetch_related("application_set").filter(pk=pk).first()
        if program is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response_data = ProgramDetailSerializer(program).data

        return Response(response_data, status=status.HTTP_200_OK)


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


class ProgramAttendanceCodeVerifyView(APIView):
    class RequestDataSerializer(serializers.Serializer):
        # FIXME: Improve comment on choice field
        type = serializers.ChoiceField(help_text="0:프로그램 시작 코드 / 1:프로그램 종료 코드", choices=AttendanceCode.CodeType.choices)
        code = serializers.CharField()

    @extend_schema(
        request=RequestDataSerializer,
        responses={
            status.HTTP_200_OK: [],
            status.HTTP_400_BAD_REQUEST: [{
                "error_code": 10001,
                "error_msg": "attendance code is incorrect"
            }],
        }
    )
    def post(self, request, pk, *args, **kwargs):
        if not Program.objects.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        program = Program.objects.get(id=pk)

        application = Application.objects.filter(program=program, student=request.user)
        if not application.exists():
            response_data = {
                "error_code": 10001,
                "error_msg": "User has no application information for the program"
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        application = application.first()

        serializer = self.RequestDataSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        code_type = serializer.validated_data.get('type')
        code = serializer.validated_data.get('code')

        if not program.verify_attendance_code(code_type, code):
            response_data = {
                "error_code": 10002,
                "error_msg": "attendance code is incorrect"
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        if code_type == 0:
            application.start_attendance()
        elif code_type == 1:
            application.end_attendance()

        return Response(status=status.HTTP_200_OK)


class LecturerListView(ListAPIView):
    class RequestDataSerializer(serializers.Serializer):
        name = serializers.CharField(help_text='사용자 실명 검색 필드. 2 글자 이상 입력시 결과 리턴')

    serializer_class = UserSerializer

    def get_queryset(self):
        username = self.request.query_params.get('name')

        if username is not None and len(username) > 1:
            queryset = Group.objects.get(name='lecturer').user_set.filter(real_name__startswith=username)
        else:
            queryset = Group.objects.none()

        return queryset

    @extend_schema(
        description='name query parameter로 사용자 실명 검색. 2 글자 이상 입력시 결과 리턴',
        responses={
            status.HTTP_200_OK: UserSerializer(many=True),
        }
    )
    def list(self, request, *args, **kwargs):
        return super(LecturerListView, self).list(request, *args, **kwargs)


class MyProgramListView(ListAPIView):
    serializer_class = ProgramSerializer

    def get_queryset(self):
        user = self.request.user

        return Program.objects.filter(application__student=user, program_end_at__gt=datetime.datetime.now())
