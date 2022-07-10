from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

from rest_framework.routers import DefaultRouter

from product.api import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/admin', permanent=False)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]
