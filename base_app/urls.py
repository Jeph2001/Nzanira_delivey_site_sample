from django.urls import path
from . import views



urlpatterns = [
    path('', views.landing_page),
    path('signup/', views.signup_page),
    path('base/', views.base_page),
    path('login/', views.login_page),
    path('location/', views.location_page),
    path('home/', views.home_page),
    path('details/<int:products_id>/', views.get_products_details, name='details'),
    path('payment/', views.payment_page),
]