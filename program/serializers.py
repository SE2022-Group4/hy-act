from rest_framework import serializers
from rest_framework.fields import IntegerField

from hy_act_server.fields import TimestampField
from program.models import Program, Category, Department


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = [
            'id',
            'name',
        ]


class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    created_at = TimestampField(help_text='프로그램 생성 시간', read_only=True)
    updated_at = TimestampField(help_text='프로그램 최종 수정 시간', read_only=True)
    apply_start_at = TimestampField(help_text='신청 접수 시작 시간')
    apply_end_at = TimestampField(help_text='신청 접수 종료 시간')
    program_start_at = TimestampField(help_text='프로그램 시작 시간')
    program_end_at = TimestampField(help_text='프로그램 종료 시간')
    recent_applicant_count = IntegerField()

    class Meta:
        model = Program
        fields = [
            'id',
            'name',
            'description',
            'created_at',
            'updated_at',
            'apply_start_at',
            'apply_end_at',
            'program_start_at',
            'program_end_at',
            'thumbnail_url',
            'location',
            'target_grade',
            'max_applicant_count',
            'sex',
            'department',
            'category',
            'recent_applicant_count',
        ]
