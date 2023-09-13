from django.urls import path
from rest_framework.routers import DefaultRouter
from ..views.product_views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    # Other app-specific URL patterns if any
]

urlpatterns += router.urls
