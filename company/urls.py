from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentViewSet, CompanyViewSet, EmployeeViewSet, AgreementViewSet, CategoryViewSet, CategoryRaymentsViewSet, EmployeeToAgreementViewSet

router = DefaultRouter()
router.register(r'agents', AgentViewSet)  # URL для агентов
router.register(r'companies', CompanyViewSet)  # URL для компаний
router.register(r'employees', EmployeeViewSet)
router.register(r'agreements', AgreementViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'category_payments', CategoryRaymentsViewSet)
router.register(r'employee_to_agreement', EmployeeToAgreementViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('agents/', views.agents, name='agents'),
    path('agents/add_agent/', views.agent_create, name='add_agent'),
    path('agents/update_agent/', views.update_agent, name='update_agent'),
    path('agents/delete_agent/', views.delete_agent, name='delete_agent'),
    path('companies/', views.companies, name='companies'),
    path('companies/add_company/', views.create_company, name='add_company'),
    path('companies/update_company/', views.update_company, name='update_company'),
    path('companies/delete_company/', views.delete_company, name='delete_company'),
    path('employees/', views.employees, name='employees'),
    path('agreements/', views.agreements, name='agreements'),
    path('employees/add_employee/', views.add_employee, name='add_employee'),
    path('employees/update_employee/', views.update_employee, name='update_employee'),
    path('employees/delete_employee/', views.delete_employee, name='delete_employee'),
    path('employees/add_category/', views.add_category, name='add_category'),
    path('agreements/add-agreement/', views.add_agreement, name='add_agreement'),
    path('agreement/add_payment/', views.add_category_payment, name='add_category_payment'),
    path('agreements/employee/', views.add_employee_to_agreement, name='add_employee_to_agreement'),
    path('search1', views.search1, name='search1'),
    path('search2', views.search2, name='search2'),
    path('search3', views.search3, name='search3'),
]


'''
path('agreements/add-agreement/', views.add_agreement, name='add_agreement'),
path('agreements/add-payments/<int:agreement_id>/', views.add_payments, name='add_payments'),




'''