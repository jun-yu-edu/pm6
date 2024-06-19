from django.shortcuts import render

from accounts.serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def register(request):
    data = request.data 
    serializer = UserSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    

# @permission_classes([IsAuthenticated])
@api_view(['GET'])
def me(request):

    user = request.user
    print(user)
    serializer = UserSerializer(user)

    return Response(serializer.data)