from rest_framework.serializers import ModelSerializer

from accounts.models import User


class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'is_admin')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)