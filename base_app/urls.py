from django.urls import path, include
from . import views








urlpatterns = [
    path('', views.landing_page),
    path('signup/', views.signup_page),
    path('base/', views.base_page),
    path('login/', views.login_page),
    path('location/', views.location_page),
    path('home/', views.home_page),
    path('details/<int:products_id>/', views.get_products_details, name='details'),
    path('payment/<int:product_id>/', views.payment_page, name='payment'),
    path('thanking/', views.thanking_page),
    path('users/', views.ListOfUser.as_view()),
    path('createuser/', views.CreateUser.as_view()),
    path('deleteuser/<int:pk>/', views.DeleteUser.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('listoflocation/', views.LocationList.as_view()),
]
