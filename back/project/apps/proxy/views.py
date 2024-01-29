import re

from django.http import JsonResponse
from fake_useragent import UserAgent
from rest_framework import permissions
from rest_framework import status

from project.abc_utils import views
from project.apps.proxy.models import Site
from . import serializer
from .handler import ProxyActions


class ProxyCreate(views.BaseReadView, views.BaseCreateView, views.BaseDeleteView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializer.SiteSerializer
    queryset = Site

    def get(self, request, *args, **kwargs) -> JsonResponse:
        response = self.queryset.objects.filter(owner=request.user).values(
            'id',
            'name',
            'site',
            'created_at',
            'traffic',
            'transition'
        )
        return JsonResponse(
            data={
                "response": self.serializer_class(instance=response, many=True).data
            },
        )

    def post(self, request, *args, **kwargs) -> JsonResponse:
        data = self.serializer_class(data=request.data)
        if not data.is_valid():
            return JsonResponse(
                data={'error': data.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        self.queryset.objects.get_or_create(
            name=data.validated_data['name'],
            site=data.validated_data['site'],
            owner=request.user
        )
        return JsonResponse(
            data={},
        )

    def delete(self, request, *args, **kwargs) -> JsonResponse:
        try:
            self.queryset.objects.get(id=request.data['id']).delete()
        except:
            pass
        return JsonResponse(
            data={},
        )


class ProxyView(views.BaseCreateView):

    def post(self, request, *args, **kwargs) -> JsonResponse:
        ua = UserAgent()
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=1,image/webp,image/apng,*/*;q=1',
            'user-Agent': ua.random,
        }
        path = request.META['PATH_INFO']
        query = request.META['QUERY_STRING'] if len(request.META['QUERY_STRING']) > 0 else None

        try:
            if path.startswith('/api/proxy/'):
                path = path[len('/api/proxy/'):]
            path = ProxyActions.clear_path(path, 'https://', 'https:/')
            path = ProxyActions.clear_path(path, 'http://', 'http:/')

            res = re.match(r'^(?:[^/?#]*/){2}[^/]+', path)
            site: Site = Site.objects.filter(
                site__contains=res.group(),
                owner=request.user,
            ).first()
            site.transition += 1

            modified_html = ProxyActions.perform_proxy_actions(site, path, query, headers)

            return JsonResponse(data={'site': modified_html}, status=200)

        except Exception as e:
            return JsonResponse(data={'error': str(e)}, status=400)
