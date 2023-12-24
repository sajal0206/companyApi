from django.db import models

company_type_choices = [
        ("IT", "IT"),
        ("Agri", "Agri"),
        ("Food", "Food"),
        ("Cosmetics", "Cosmetics")
        ]

gender_choices = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"),
        ]


# company model
class Company(models.Model):
    company_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 50)
    about = models.TextField()
    type_of_comp = models.CharField(max_length = 50, choices = company_type_choices)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)
    
# user model
class CompanyUser(models.Model):
    user_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 100, choices = gender_choices)
    age = models.IntegerField(default = 0)
    bio = models.TextField()
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)