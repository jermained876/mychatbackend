from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializer import UserCreateSerializer, UserCurrentSerializer
from rest_framework.permissions import IsAuthenticated


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserCurrent(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serial = UserCurrentSerializer(user, many=False)
        return Response(serial.data)


class testing(APIView):

    def get(self,request):
        return Response('TEstingbig')