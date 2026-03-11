from django.urls import include, path
from rest_framework.routers import DefaultRouter

from spm.companies.api.v1.views import CompanyViewSet

app_name = "companies"

router = DefaultRouter()
router.register("company", CompanyViewSet, basename="company")

urlpatterns = [
    path("", include(router.urls)),
]
