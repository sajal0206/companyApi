from rest_framework import viewsets, generics
from apis.models import Company, CompanyUser
from apis.serializers import CompanySerializer, CompanyViewSerializer, CompanyUserSerializer, CompanyUserViewSerializer

# Create your views here.

# company viewSet
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# company user viewSet
class CompanyUserViewSet(viewsets.ModelViewSet):
    queryset = CompanyUser.objects.all()
    serializer_class = CompanyUserSerializer
    permission_classes = [] # used to allow or disallow CRUD to be used without token
    
class CompanyViewListApiView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyViewSerializer

class CompanyUserViewListApiView(generics.ListAPIView):
    queryset = CompanyUser.objects.all()
    serializer_class = CompanyUserViewSerializer