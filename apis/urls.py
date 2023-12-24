
# Routers provide an easy way of automatically determining the URL conf.
from django.urls import include, path
from rest_framework import routers
from apis.views import CompanyViewSet, CompanyUserViewSet, CompanyViewListApiView, CompanyUserViewListApiView


router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'company-users', CompanyUserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('get-all-company-users', CompanyUserViewListApiView.as_view()),
    path('get-all-companies', CompanyViewListApiView.as_view()),
]