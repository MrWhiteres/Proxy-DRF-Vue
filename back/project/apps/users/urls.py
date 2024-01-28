from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from project.apps.users import views

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('new_token/', TokenRefreshView.as_view(), name='new_token'),
]
