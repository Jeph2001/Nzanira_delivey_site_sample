from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page),
    path('signup/', views.signup_page),
    path('base/', views.base_page),
    path('login/', views.login_page),
]