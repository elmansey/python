from django.db import models

# Create your models here.
from departments.models import  Department
from django.shortcuts import render, redirect , reverse


class Employee(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    dept = models.ForeignKey(Department, null=True, blank=True,on_delete=models.CASCADE, related_name='dept_id')

    def __str__(self):
        return self.name
    
    @classmethod
    def get_all_employees(cls):
        return cls.objects.all()
    
    @classmethod
    def get_employee(cls , id ):
        return cls.objects.get(id=id)
    


    def get_delete_url(self):
        url = reverse('employees.delete', args=[self.id])
        return url
    
    def get_show_url(self):
        url = reverse('employees.show', args=[self.id])
        return url
