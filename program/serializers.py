from rest_framework import serializers

from hy_act_server.fields import TimestampField
from program.models import Program


class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    created_at = TimestampField(read_only=True)
    updated_at = TimestampField(read_only=True)
    apply_start_at = TimestampField()
    apply_end_at = TimestampField()
    class_start_at = TimestampField()
    class_end_at = TimestampField()

    class Meta:
        model = Program
        fields = [
            'name',
            'description',
            'created_at',
            'updated_at',
            'apply_start_at',
            'apply_end_at',
            'class_start_at',
            'class_end_at',
        ]
