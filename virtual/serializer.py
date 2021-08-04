from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "password"]


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=50, required=True, write_only=True
    )
    password = serializers.CharField(max_length=50, required=True, write_only=True)
    

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("old_password", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        print("user", user)
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"}
            )
        return value

    def update(self, instance, validated_data):
        user = User.objects.get(username=self.context["request"].user)
        user.set_password(validated_data["password"])
        user.save()

        return user


class SendMailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=60)
    message = serializers.CharField(max_length=60)
