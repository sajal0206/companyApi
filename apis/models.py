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
    company_logo = models.ImageField(blank = True, null = True, upload_to="images/company_logos/")
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 50, blank = True, default = "")
    about = models.TextField(blank = True, default = "")
    type_of_comp = models.CharField(max_length = 50, choices = company_type_choices, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)

    def __str__(self) -> str:
        return self.name + " | " + self.location
    
# user model
class CompanyUser(models.Model):
    user_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    image = models.ImageField(blank = True, null = True, upload_to="images/user_images/")
    gender = models.CharField(max_length = 100, choices = gender_choices, blank = True)
    age = models.IntegerField(default = 0)
    bio = models.TextField(blank = True, default = "")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)
    
    def __str__(self) -> str:
        return self.name + " ( Age: " + str(self.age) + " )"