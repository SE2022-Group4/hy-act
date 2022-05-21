from datetime import datetime

from django.utils.timezone import make_aware
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers


@extend_schema_field(OpenApiTypes.NUMBER)
class TimestampField(serializers.Field):
    def to_internal_value(self, data):
        return make_aware(datetime.fromtimestamp(data))

    def to_representation(self, value):
        return int(value.timestamp())
