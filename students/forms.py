from django import forms
from .models import Student,Internship,Mentor,Company

class CombinedForm(forms.Form):
    # Fields for Internship
    internship_title = forms.CharField(max_length=50)
    internship_year = forms.IntegerField()
    internship_mode = forms.CharField(max_length=50)
    internship_description = forms.CharField(widget=forms.Textarea)
    internship_stipend = forms.IntegerField()
    internship_duration = forms.IntegerField()
    internship_ppo = forms.CharField(max_length=50)
    internship_certificate = forms.URLField(max_length=200)

    # Fields for Mentor
    mentor_internal_name = forms.CharField(max_length=50)
    mentor_external_name = forms.CharField(max_length=50)
    mentor_mobile = forms.CharField(max_length=10)
    mentor_email = forms.EmailField(max_length=254)

    # Fields for Company
    company_name = forms.CharField(max_length=50)
    company_address = forms.CharField(widget=forms.Textarea)
    company_website = forms.URLField(max_length=200)

    # Fields for Student
    student_roll_no = forms.IntegerField()
    student_academic_year = forms.CharField(max_length=50)
    student_name = forms.CharField(max_length=50)
    student_division = forms.CharField(max_length=50)
    student_department = forms.CharField(max_length=20)
    student_email = forms.EmailField(max_length=254)
    student_mobile = forms.CharField(max_length=10)
