from django.shortcuts import render, redirect , reverse
from  employees.models import Employee
from  django.http import HttpResponse
# Create your views here.

def employeesPage(request):
    return render(request, 'employees.html')


def employees_list(request):
    employees = Employee.get_all_employees()
    return render(request,'employees.html',context={"allemployees": employees})


def delete_employees(request, id ):
    employee = Employee.get_employee(id) 
    employee.delete()
    redirect_url = reverse('employees.index')
    return redirect(redirect_url)


def show_employee(request, id ):
    employee = Employee.get_employee(id) 
    return render(request , 'show_employee.html',context={"employee": employee})