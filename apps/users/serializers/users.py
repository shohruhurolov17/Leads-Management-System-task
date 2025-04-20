from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken


class LoginSerializer(serializers.Serializer):

    password = serializers.CharField()

    username = serializers.CharField()

    def validate(self, attrs):

        request = self.context['request']
        
        password = attrs['password']

        username = attrs['username']

        user = authenticate(
            username=username,
            password=password,
            request=request
        )

        if user is None:

            raise serializers.ValidationError(_('Invalid password or username.'))
        
        attrs['user'] = user

        return attrs


class UserDetailSerializer(serializers.ModelSerializer):

    access_token = serializers.SerializerMethodField()

    refresh_token = serializers.SerializerMethodField()

    class Meta:

        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'access_token',
            'refresh_token'
        )

    def get_access_token(self, instance) -> str:

        return str(RefreshToken.for_user(instance).access_token)
    
    def get_refresh_token(self, instance) -> str:

        return str(RefreshToken.for_user(instance))