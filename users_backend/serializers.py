from rest_framework import serializers
from users_backend.models import User


class UserSerializersBackend(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.CharField(max_length=30, min_length=8)
    phone = serializers.CharField(min_length=12, max_length=13)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(min_length=8, max_length=25)

    class Meta:
        model = User
        fields = ["id", "username", "phone", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user


class RegisterSerializersBackend(serializers.ModelSerializer):
    password = serializers.CharField(max_length=25, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "phone", "password"]

    def validate(self, attrs):
        email = attrs.get("email", None)
        phone = attrs.get("phone", None)
        username = attrs.get("username", None)

        if not username.isalnum():
            raise serializers.ValidationError(self.default_error_messages)
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class EmailVerificationSerializersBackend(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ["token"]


class LoginSerializersBackend(serializers.Serializer):
    phone = serializers.CharField(max_length=30)
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ["phone", "password"]
