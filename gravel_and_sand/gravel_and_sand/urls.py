"""gravel_and_sand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app_first__gravel_and_sand.views import ProductsViewSet, auth, new_order, OrdersViewSet, save_new_order, \
    AreasViewSet

router = SimpleRouter()

router.register(r'get_products', ProductsViewSet, basename='get_products')
router.register(r'get_areas', AreasViewSet, basename='get_areas')
router.register(r'order', OrdersViewSet, basename='order')
#router.register(r'new_order/get_products', ProductsViewSet, basename='get_products')
#router.register(r'get_products$', ProductsViewSet, basename='get_products')

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),
    path('auth/', auth, name='auth/'),

    path('new_order/', new_order, name='new_order/'),
    path('save_new_order/', save_new_order, name='save_new_order')
]

urlpatterns += router.urls