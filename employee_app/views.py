from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import Employee
from django.urls import reverse_lazy
# Create your views here.
# class DisplayView(TemplateView):
#     template_name= 'index.html'

class EmployeeCreateView(CreateView):
   model=Employee
   fields="__all__"
   template_name= "index.html"
   success_url=reverse_lazy("employee_create")

class EmployeeListView(ListView):
   model=Employee
   template_name= "emp_list.html"
   context_object_name='employees'

class EmployeeUpdateView(UpdateView):
   model=Employee
   fields="__all__"
   template_name= "emp_update.html"
   context_object_name='employee'
   success_url=reverse_lazy("employee_list")

class EmployeeDeleteView(DeleteView):
   model=Employee
   template_name= "employee_confirm_delete.html"
   success_url=reverse_lazy("employee_list")

class EmployeeDetailView(DetailView):
   model=Employee
   template_name= "employee_detail.html"
   context_object_name='employee'