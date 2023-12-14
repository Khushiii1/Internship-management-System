from django.contrib import admin
from .models import Student,Internship,Mentor,Company

# Register your models here.
admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Internship)
admin.site.register(Company)
