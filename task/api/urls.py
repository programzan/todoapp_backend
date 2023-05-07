from django.urls import include, path
from rest_framework.routers import DefaultRouter

from task.api.views import AssignedTaskViewSet

app_name = 'api_task'

router = DefaultRouter()
router.register('my', AssignedTaskViewSet, 'my-tasks')

urlpatterns = [
    path('', include(router.urls))
]