from django.contrib import admin
from apis.models import Company, CompanyUser

# Register your models here.
admin.site.register(Company)
admin.site.register(CompanyUser)