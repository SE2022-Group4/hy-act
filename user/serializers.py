from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

from user.models import Department, Major

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    departments = DepartmentSerializer(many=True)
    majors = MajorSerializer(many=True)

    class Meta:
        model = User
        fields = [
            'username',
            'real_name',
            'email',
            'groups',
            'telephone',
            'departments',
            'majors',
        ]


class UserSigninSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
