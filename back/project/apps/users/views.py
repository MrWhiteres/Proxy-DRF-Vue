from django.http import JsonResponse
from rest_framework import permissions
from rest_framework import status

from project.abc_utils import views
from . import serializers
from .helpers.controller import login
from .helpers.controller import registration
from .helpers.sub import logout


class RegistrationView(views.BaseCreateView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request, *args, **kwargs) -> JsonResponse:
        check = self.validate(request)

        if not check.success:
            return self.response(check.error, status.HTTP_400_BAD_REQUEST)

        result = registration(check)
        if not result.success:
            return self.response(result.error, status.HTTP_400_BAD_REQUEST)
        return self.response(result.data, status.HTTP_201_CREATED)


class LoginView(views.BaseCreateView):
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs) -> JsonResponse:
        check = self.validate(request)
        if not check.success:
            return self.response(check.error, status.HTTP_400_BAD_REQUEST)

        result = login(check)
        if not result.success:
            return self.response(result.error, status.HTTP_400_BAD_REQUEST)
        return self.response(result.data, status.HTTP_200_OK)


class LogoutView(views.BaseCreateView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs) -> JsonResponse:
        logout(request.data.get('refresh'))
        return self.response({}, status.HTTP_200_OK)


class ProfileView(views.BaseReadView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs) -> JsonResponse:
        return self.response({}, status.HTTP_200_OK)
