from rest_framework import serializers

from apis.models import Company, CompanyUser

# create all serialiers here

# company serializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

# company custom view serializer
class CompanyViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["company_id",
                  "name",
                  "type_of_comp",
                  ]

# company user serializer
class CompanyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = "__all__"

# company user custom view serializer

class companyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["name"]
    
class CompanyUserViewSerializer(serializers.ModelSerializer):
    company = companyNameSerializer()
    class Meta:
        model = CompanyUser
        fields = ["user_id", "name", "gender", "age", "bio", "company", "created_at", "updated_at", "is_active",]