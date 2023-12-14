from django.db import models
from django.forms import ModelForm
from phone_field import PhoneField

# Create your models here.
class Internship(models.Model):
    id=models.AutoField(primary_key=True)
    Title=models.CharField( max_length=50) 
    year = models.PositiveIntegerField()
    Mode = models.CharField( max_length=50)
    Description=models.TextField()
    Stripend=models.IntegerField()
    Duration=models.IntegerField()
    PPO=models.CharField(max_length=50)
    certificate=models.URLField( max_length=200)
    def __str__(self):
        return self.Title
    
class Mentor(models.Model):
    id=models.AutoField(primary_key=True)
    Internal_Mentor=models.CharField( max_length=50)
    External_Mentor=models.CharField( max_length=50)
    Mobile=models.CharField(max_length=10)
    Email=models.EmailField( max_length=254)
    
    def __str__(self):
        return self.Internal_Mentor
    
class Company(models.Model):
    id=models.AutoField(primary_key=True)
    company_name=models.CharField( max_length=50) 
    company_address=models.TextField()
    company_website=models.URLField( max_length=200)
    
    def __str__(self):
        return self.company_name
    
class Student(models.Model):
    #Sr_No =models.IntegerField()
    Roll_No=models.IntegerField(primary_key=True)
    Academic_Year=models.CharField(max_length=50)
    Name = models.CharField( max_length=50)
    Division=models.CharField( max_length=50)
    Department=models.CharField(max_length=20)
    email=models.EmailField( max_length=254) 
    Mobile=models.CharField(max_length=10)
    internship= models.ForeignKey(Internship, on_delete=models.CASCADE)
    mentor= models.ForeignKey(Mentor, on_delete=models.CASCADE)
    company= models.ForeignKey(Company, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.Name
    

    
