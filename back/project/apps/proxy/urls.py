from django.urls import path
from django.urls import re_path

from project.apps.proxy import views

urlpatterns = [
    path('proxy/', views.ProxyCreate.as_view(), name='proxy-create'),
    re_path(
        r'^proxy/(.*$)',
        views.ProxyView.as_view(),
        name='proxy-base'
    ),
]
