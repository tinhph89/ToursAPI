from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import ToursViewSet

router = DefaultRouter()
router.register('api', ToursViewSet)

urlpatterns = [
    path('', include(router.urls))
]