"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from virtual.urls import router
from rest_framework.authtoken.views import obtain_auth_token

from virtual.views import UserLoginView, LogoutView, ChangePasswordView, SendMailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('gettoken/', obtain_auth_token),
    path("user-login/", UserLoginView.as_view(), name="user_login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("change_password/<int:pk>/",
        ChangePasswordView.as_view(),
        name="auth_change_password",
    ),
    path("send-mail/", SendMailView.as_view(), name="send-mail"),
]
