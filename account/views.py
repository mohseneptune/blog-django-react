from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_object_or_404

from account.serializers import UserSerializer

User = get_user_model()


@permission_classes([IsAdminUser])
@api_view()
def user_list_view(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True, context={"request": request})
    return Response(data=serializer.data, status=HTTP_200_OK)


@permission_classes([IsAdminUser])
@api_view()
def user_detail_view(request, pk):
    users = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(users, context={"request": request})
    return Response(data=serializer.data, status=HTTP_200_OK)
