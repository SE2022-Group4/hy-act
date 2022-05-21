from rest_framework import serializers

from hy_act_server.fields import TimestampField
from program.models import Program


class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    created_at = TimestampField(help_text='프로그램 생성 시간', read_only=True)
    updated_at = TimestampField(help_text='프로그램 최종 수정 시간', read_only=True)
    apply_start_at = TimestampField(help_text='신청 접수 시작 시간')
    apply_end_at = TimestampField(help_text='신청 접수 종료 시간')
    program_start_at = TimestampField(help_text='프로그램 시작 시간')
    program_end_at = TimestampField(help_text='프로그램 종료 시간')

    class Meta:
        model = Program
        fields = [
            'name',
            'description',
            'created_at',
            'updated_at',
            'apply_start_at',
            'apply_end_at',
            'program_start_at',
            'program_end_at',
        ]
