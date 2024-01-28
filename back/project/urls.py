from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('project.apps.users.urls')),
    # path('api/', include('project.apps.proxy.urls')),
]
