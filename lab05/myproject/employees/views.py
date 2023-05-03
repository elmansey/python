from django.shortcuts import render

# Create your views here.

def employeesPage(request):
    return render(request, 'employees.html')