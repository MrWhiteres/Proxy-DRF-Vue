from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass

from django.http import JsonResponse
from rest_framework import generics
from rest_framework import views
from rest_framework.request import Request
from rest_framework.serializers import Serializer

from project.abc_utils import data


class BaseView(views.APIView, ABC):
    """Abstract base class for all API views."""
    serializer_class: Serializer = Serializer
    data_class: dataclass = data.Result

    @staticmethod
    def response(response: dict, status_response: int) -> JsonResponse:
        return JsonResponse(
            data=response,
            status=status_response
        )

    def validate(self, request: Request) -> data.Result:
        valid = self.serializer_class(data=request.data)

        if not valid.is_valid():
            return self.data_class(
                error=valid.errors
            )
        return self.data_class(
            data=valid.validated_data,
            success=True
        )


class BaseReadView(BaseView, generics.RetrieveAPIView):
    """Abstract base class for all read API views."""

    @abstractmethod
    async def get(self, request, *args, **kwargs) -> JsonResponse:
        """Abstract method for all read API views."""


class BaseCreateView(BaseView, generics.CreateAPIView):
    """Abstract base class for all create API views."""

    @abstractmethod
    async def post(self, request, *args, **kwargs) -> JsonResponse:
        """Abstract method for all create API views."""


class BaseDeleteView(BaseView, generics.DestroyAPIView):
    """Abstract base class for all delete API views."""

    @abstractmethod
    async def delete(self, request, *args, **kwargs) -> JsonResponse:
        """Abstract method for all delete API views."""


class BaseUpdateView(BaseView, generics.UpdateAPIView):
    """Abstract base class for all update API views."""

    @abstractmethod
    async def put(self, request, *args, **kwargs) -> JsonResponse:
        """Abstract method for all update API views."""
