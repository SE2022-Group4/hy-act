from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import Group
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status, views
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Major
from .serializers import UserSerializer, GroupSerializer, UserSigninSerializer, MajorSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@extend_schema(
        request=UserSigninSerializer,
        responses=UserSigninSerializer,
        # more customizations
    )
@api_view(["POST"])
@permission_classes((AllowAny,))
def signin(request):
    signin_serializer = UserSigninSerializer(data=request.data)
    if not signin_serializer.is_valid():
        return Response(signin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(
        username=signin_serializer.data['username'],
        password=signin_serializer.data['password']
    )
    if not user:
        return Response({'detail': 'Invalid Credentials or activate account'}, status=status.HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)

    user_serialized = UserSerializer(user, context={'request': request})

    return Response({
        'user': user_serialized.data,
        'token': token.key,
    }, status=status.HTTP_200_OK)


class SessionUserInfoView(views.APIView):
    def get(self, request, *args, **kwargs):
        user = request.user

        user_serialized = UserSerializer(user, context={'request': request})

        return Response(user_serialized.data, status=status.HTTP_200_OK)


class MajorListView(ListAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
