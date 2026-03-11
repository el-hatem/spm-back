from django.urls import include, path

v1 = [
    path("companies/", include("spm.companies.api.v1.urls", namespace="companies")),
    path("portal/", include("spm.portal.api.v1.urls", namespace="portal")),
    path("clients/", include("spm.clients.api.v1.urls", namespace="clients")),
]

urlpatterns = [
    path("v1/", include((v1, "v1"), namespace="v1")),
]
