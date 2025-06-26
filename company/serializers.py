# company/serializers.py
from rest_framework import serializers
from .models import Agent, Company, Employee, Agreement, Category, CategoryPayment, EmployeeToAgreement

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['agent_id', 'agent_name', 'agent_passport_id', 'agent_passport_number', 'agent_passport_date']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AgreementS(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'

class CategoryS(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryPaymentS(serializers.ModelSerializer):
    class Meta:
        model = CategoryPayment
        fields = '__all__'

class EmployeeToAgreementS(serializers.ModelSerializer):
    class Meta:
        model = EmployeeToAgreement
        fields = '__all__'