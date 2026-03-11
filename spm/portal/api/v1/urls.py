from django.urls import include, path
from rest_framework.routers import DefaultRouter

from spm.portal.api.v1.views import ApprovalViewSet

app_name = "portal"

router = DefaultRouter()

router.register("approvals", ApprovalViewSet, basename="approvals")

urlpatterns = [
    path("", include(router.urls)),
]
