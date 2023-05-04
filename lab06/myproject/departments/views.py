from django.shortcuts import render
from  departments.models import Department

# Create your views here.


def departmentsPage(request):
    return render(request, 'departments.html')


def departments_list(request):
    departments = Department.get_all_departments()
    return render(request,'departments.html',context={"alldepartments": departments}  )