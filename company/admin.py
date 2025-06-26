from django.contrib import admin
from .models import Agent, Agreement, Category, CategoryPayment, Company, Employee, EmployeeToAgreement

admin.site.register(Agent)
admin.site.register(Agreement)
admin.site.register(Category)
admin.site.register(CategoryPayment)
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(EmployeeToAgreement)