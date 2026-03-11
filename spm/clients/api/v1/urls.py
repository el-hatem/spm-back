from django.urls import include, path
from rest_framework.routers import DefaultRouter

from spm.clients.api.v1.views import ClientViewSet

app_name = "clients"

router = DefaultRouter()
router.register("client", ClientViewSet, basename="client")

urlpatterns = [
    path("", include(router.urls)),
]
