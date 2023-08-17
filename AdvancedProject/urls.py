"""
URL configuration for AdvancedProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from base_app.views import ProductsViewSet, PaymentsViewSet, LocationViewSet
from quickstart_on_api.views import UserViewSet, GroupViewSet
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='This is My First API',
        default_version='v1',
        description='this API is for retrieving the data from the Nzanira App.',
        terms_of_service='this API is monetized, means you have to pay',
        contact=openapi.Contact(email='josephmaniragaba9@gmail.com'),
        license=openapi.License(name='This is not license, it is just a words. in fact am just testing'),
    ),
    public=True,
    # permission_classes=permissions.AllowAny,
)





router = routers.DefaultRouter()
router.register(r'product', ProductsViewSet)
router.register(r'payment', PaymentsViewSet)
router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'location', LocationViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base_app.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('base_app/', include(router.urls)),
    path('accounts/', include('allauth.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





