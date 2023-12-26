from rest_framework import viewsets, generics
from apis.models import Company, CompanyUser
from apis.serializers import CompanySerializer, CompanyViewSerializer, CompanyUserSerializer, CompanyUserViewSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

# company viewSet
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# function to get all users of particular company
    @action(detail=True, methods=['get'])
    def users(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            user = CompanyUser.objects.filter(company = company)
            users_serializer = CompanyUserSerializer(user, many = True,context = {'request' : request})
            return Response(users_serializer.data)
        except Exception as e:
            return Response({"message":str(e)})
        

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