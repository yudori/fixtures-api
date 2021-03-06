from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from accounts.v1.serializers import RegistrationSerializer


class RegisterVeiw( mixins.CreateModelMixin, generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        """Register a new user."""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)   # returns appropriate response with error status code if invalid
        user = serializer.create(serializer.validated_data)
        data = {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_admin': user.is_admin,
        }
        return Response(data=data, status=status.HTTP_201_CREATED)


class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        """Log an existing user in by returning token."""
        formatted_data = request.data.copy()
        formatted_data['username'] = request.data.get('email')
        serializer = self.serializer_class(data=formatted_data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'email': user.email,
            'token': token.key
        })
