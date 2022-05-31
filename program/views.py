from unicodedata import category
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.filters import SearchFilter
from django.http import Http404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from program.models import Category, Program, Department
from program.serializers import CategorySerializer, ProgramSerializer, DepartmentSerializer
from user import serializers


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
        parameters=[
            CategorySerializer
        ],
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
    def get(self):
        departments = Department.objects.all()
        departments_serialized = DepartmentSerializer(departments, many=True)
        return Response(departments_serialized.data)

    @extend_schema(
        parameters=[
            DepartmentSerializer
        ],
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
