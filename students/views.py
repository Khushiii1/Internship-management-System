from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Student,Mentor,Internship,Company
from .forms import CombinedForm

def index(request):
    return render(request,'students/index.html',{
        'students':Student.objects.all(),'mentor':Mentor.objects.all(),'intern':Internship.objects.all(),'company':Company.objects.all()
    })

def view_student(request,id):
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = CombinedForm(request.POST)
        if form.is_valid():
            # Create or retrieve Internship
            internship, _ = Internship.objects.get_or_create(
                Title=form.cleaned_data['internship_title'],
                year=form.cleaned_data['internship_year'],
                Mode=form.cleaned_data['internship_mode'],
                Description=form.cleaned_data['internship_description'],
                Stripend=form.cleaned_data['internship_stipend'],
                Duration=form.cleaned_data['internship_duration'],
                PPO=form.cleaned_data['internship_ppo'],
                certificate=form.cleaned_data['internship_certificate']
            )
            
            # Create or retrieve Mentor
            mentor, _ = Mentor.objects.get_or_create(
                Internal_Mentor=form.cleaned_data['mentor_internal_name'],
                External_Mentor=form.cleaned_data['mentor_external_name'],
                Mobile=form.cleaned_data['mentor_mobile'],
                Email=form.cleaned_data['mentor_email']
            )
            
            # Create or retrieve Company
            company, _ = Company.objects.get_or_create(
                company_name=form.cleaned_data['company_name'],
                company_address=form.cleaned_data['company_address'],
                company_website=form.cleaned_data['company_website']
            )
            
            # Create Student
            student = Student(
                Roll_No=form.cleaned_data['student_roll_no'],
                Academic_Year=form.cleaned_data['student_academic_year'],
                Name=form.cleaned_data['student_name'],
                Division=form.cleaned_data['student_division'],
                Department=form.cleaned_data['student_department'],
                email=form.cleaned_data['student_email'],
                Mobile=form.cleaned_data['student_mobile'],
                internship=internship,
                mentor=mentor,
                company=company
            )
            student.save()

            # Add a success flag for displaying a success message
            success = True
        else:
            success = False
    else:
        form = CombinedForm()
        success = False

    return render(request, 'students/add.html', {'form': form, 'success': success})

def edit(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        form = CombinedForm(request.POST)

        if form.is_valid():
            # Update Student model
            student.Roll_No = form.cleaned_data['student_roll_no']
            student.Academic_Year = form.cleaned_data['student_academic_year']
            student.Name = form.cleaned_data['student_name']
            student.Division = form.cleaned_data['student_division']
            student.Department = form.cleaned_data['student_department']
            student.email = form.cleaned_data['student_email']
            student.Mobile = form.cleaned_data['student_mobile']
            student.save()

            # Update Internship model
            internship, _ = Internship.objects.update_or_create(
                id=student.internship.id,
                defaults={
                    'Title': form.cleaned_data['internship_title'],
                    'year': form.cleaned_data['internship_year'],
                    'Mode': form.cleaned_data['internship_mode'],
                    'Description': form.cleaned_data['internship_description'],
                    'Stripend': form.cleaned_data['internship_stipend'],
                    'Duration': form.cleaned_data['internship_duration'],
                    'PPO': form.cleaned_data['internship_ppo'],
                    'certificate': form.cleaned_data['internship_certificate'],
                }
            )

            # Update Mentor model
            mentor, _ = Mentor.objects.update_or_create(
                id=student.mentor.id,
                defaults={
                    'Internal_Mentor': form.cleaned_data['mentor_internal_name'],
                    'External_Mentor': form.cleaned_data['mentor_external_name'],
                    'Mobile': form.cleaned_data['mentor_mobile'],
                    'Email': form.cleaned_data['mentor_email'],
                }
            )

            # Update Company model
            company, _ = Company.objects.update_or_create(
                id=student.company.id,
                defaults={
                    'company_name': form.cleaned_data['company_name'],
                    'company_address': form.cleaned_data['company_address'],
                    'company_website': form.cleaned_data['company_website'],
                }
            )

            return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
    else:
        initial_data = {
            'student_roll_no': student.Roll_No,
            'student_academic_year': student.Academic_Year,
            'student_name': student.Name,
            'student_division': student.Division,
            'student_department': student.Department,
            'student_email': student.email,
            'student_mobile': student.Mobile,
            'internship_title': student.internship.Title,
            'internship_year': student.internship.year,
            'internship_mode': student.internship.Mode,
            'internship_description': student.internship.Description,
            'internship_stipend': student.internship.Stripend,
            'internship_duration': student.internship.Duration,
            'internship_ppo': student.internship.PPO,
            'internship_certificate': student.internship.certificate,
            'mentor_internal_name': student.mentor.Internal_Mentor,
            'mentor_external_name': student.mentor.External_Mentor,
            'mentor_mobile': student.mentor.Mobile,
            'mentor_email': student.mentor.Email,
            'company_name': student.company.company_name,
            'company_address': student.company.company_address,
            'company_website': student.company.company_website,
        }
        form = CombinedForm(initial=initial_data)

    return render(request, 'students/edit.html', {'form': form, 'student': student})
