from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.api.views import UserViewSet

app_name = 'api_core'

router = DefaultRouter()
router.register('users', UserViewSet, 'users')

urlpatterns = [
    path('', include(router.urls))
]