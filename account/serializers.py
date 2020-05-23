from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from . import models
class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer for creating user objects."""

    tokens = serializers.SerializerMethodField()

    class Meta:
        model = models.CustomUser
        fields = ('id', 'password', 'email', 'tokens')
        extra_kwargs = {'password': {'write_only': True}}

    def get_tokens(self, user):
        tokens = RefreshToken.for_user(user)
        refresh = text_type(tokens)
        access = text_type(tokens.access_token)
        data = {
            "refresh": refresh,
            "access": access
        }
        return data

    def create(self, validated_data):
        user = models.CustomUser(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()    
        return user