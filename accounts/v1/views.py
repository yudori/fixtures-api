from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.v1.serializers import RegistrationSerializer


class RegisterVeiw(APIView):

    def post(self, request, format=None):
        """
        Register a new user.
        """
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)   # returns appropriate response with error status code if invalid
        data = serializer.create(serializer.validated_data)
        return Response(data=data, status=status.HTTP_201_CREATED)
