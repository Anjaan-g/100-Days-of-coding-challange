from rest_framework import permissions, generics, serializers
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from . import models
from django import forms

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    widgets = {
      'password': forms.PasswordInput()
    }
    class Meta:
        model = models.CustomUser
        fields = (
            'email', 'password', 'first_name', 'last_name', 'phone_no'
        )
        lookup_field = 'email'
        write_only_fields = ('password')
        # read_only_fields = ('is_retailer',)
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return models.CustomUser.objects.all()
        else:
            return self.request.user
    
    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone_no = validated_data['phone_no']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '__all__'

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

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = (
            'email',
            'password',
        )
    
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8,write_only=True)
    widgets = {
      'password': forms.PasswordInput()
    }
    def post(self, email, password):
        email = self.validated_data('email')
        password = self.validated_data('password')
        
    # def login():
    #     email = get_validated_data['email']