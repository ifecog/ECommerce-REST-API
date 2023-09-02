from django.urls import path
from rest_framework.routers import DefaultRouter
from ..views.user_views import UserViewSet, MyTokenObtainPairView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('users/login/', MyTokenObtainPairView.as_view(), name='token-obtain-pair'),
    # Other app-specific URL patterns if any
]

urlpatterns += router.urls

# from django.urls import path
# from .views import UserViewSet

# urlpatterns = [
#     path('users/', UserViewSet.as_view({
#         'post': 'signup',
#         'get': 'list',
#         # 'get': 'get_personal_details'       
#     })),
#     path('users/<str:pk>/', UserViewSet.as_view({
#         'get': 'retrieve',
#         'put': 'update',
#         'delete': 'destroy'
#     }))
        
# ]