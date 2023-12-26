from django.contrib import admin
from apis.models import Company, CompanyUser

# custom admin views
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type_of_comp',)
    search_fields = ('name', 'location',)

class CompanyUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'company',)
    search_fields = ('name', 'company',)
    list_filter = ('company',)
    
    
# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyUser, CompanyUserAdmin)