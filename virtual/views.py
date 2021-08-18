from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, EmailMessage
from backend.settings import EMAIL_HOST_USER
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from virtual.serializer import UserSerializer, UserLoginSerializer, ChangePasswordSerializer, SendMailSerializer
from rest_framework import viewsets, status, generics
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class UserLoginView(APIView):
    """This view returns the login of user"""

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            try:
                u_name = data.get("username", None)
                pword = data.get("password", None)
                get_user = User.objects.get(username=u_name)
                user = authenticate(username=get_user, password=pword)
                if not user:
                    return Response(
                        {"error": "Invalid Credential"},
                        status=status.HTTP_404_NOT_FOUND,
                    )

                try:
                    token = Token.objects.get(user=user.id)
                except Token.DoesNotExist:
                    return Response(
                        {"Invalid": "Unauthenticated user"},
                        status=status.HTTP_404_NOT_FOUND,
                    )
                if user is not None:
                    if user.is_active:
                        return Response(
                            {
                                "Success": "User successfully logged in.",
                                "token": token.key,
                                "id": user.id,
                            },
                            status=status.HTTP_200_OK,
                        )
                    else:
                        return Response(status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response(
                        "User doesn't exist", status=status.HTTP_404_NOT_FOUND
                    )

            except User.DoesNotExist:
                return Response(
                    {"error": "Invalid Credential"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response("Field is required", status=status.HTTP_404_NOT_FOUND)

        def login(self, request, format=None):
            if request.user.is_authenticated:
                return Response("Loginin to create room", status=status.HTTP_200_OK)
            else:
                return Response("Loginin to create room", status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):

    """expires the logg in session of user"""

    def get(self, request, format=None):
        # using Django logout
        logout(request)
        return Response(
            {"success": ("Successfully logged out.")}, status=status.HTTP_200_OK
        )


class ChangePasswordView(generics.UpdateAPIView):
    """
    user password reset
    """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer


class SendMailView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SendMailSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            email = data.get("email")
            print(email)
            message = data.get("message")
            send_mail(
                "Virtual conference request",
                "You can use this link to join the virtual conference. {}".format(message),
                EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return Response({"success": "Message sent successfully"})
        return Response({"success": "Failed"}, status=status.HTTP_400_BAD_REQUEST)


