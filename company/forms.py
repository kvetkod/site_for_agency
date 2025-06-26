from django import forms
from .models import Employee, Company, Agent, Category, Agreement, CategoryPayment, EmployeeToAgreement

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent  # Assuming you have a model named 'Agent'
        fields = ['agent_name', 'agent_passport_id', 'agent_passport_number', 'agent_passport_date']
        widgets = {
            'agent_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ФИО'}),
            'agent_passport_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер паспорта'}),
            'agent_passport_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите идентификационный номер паспорта'}),
            'agent_passport_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Выберите дату выдачи паспорта'}),
        }


class UpdateAgentForm(forms.ModelForm):
    agent_id = forms.ModelChoiceField(
        queryset=Agent.objects.all(),  # List of existing agents
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="ID агента"
    )

    class Meta:
        model = Agent  # Assuming you have a model named 'Agent'
        fields = ['agent_id', 'agent_name', 'agent_passport_id', 'agent_passport_number', 'agent_passport_date']
        widgets = {
            'agent_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ФИО'}),
            'agent_passport_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер паспорта'}),
            'agent_passport_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите идентификационный номер паспорта'}),
            'agent_passport_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Выберите дату выдачи паспорта'}),
        }


class DeleteAgentForm(forms.Form):
    agent_id  = forms.ModelChoiceField(
        queryset=Agent.objects.all(),  # Список существующих сотрудников
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="ID агента"
    )

    class Meta:
        model = Agent
        fields = ['agent_id']



class AddCompany(forms.ModelForm):
    class Meta:
        model = Company  # Assuming you have a model named 'Company'
        fields = ['company_number', 'company_full_name', 'company_name', 'company_address', 'company_bank_number', 'company_specialization']
        widgets = {
            'company_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите код компании'}),
            'company_full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите полное наименование'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите краткое наименование'}),
            'company_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите адрес компании'}),
            'company_bank_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер банка'}),
            'company_specialization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите специализацию'}),
        }


class UpdateCompany(forms.ModelForm):
    company_id = forms.ModelChoiceField(
        queryset=Company.objects.all(),  # List of existing companies
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='ID компании'
    )

    class Meta:
        model = Company  # Assuming you have a model named 'Company'
        fields = ['company_id', 'company_number', 'company_full_name', 'company_name', 'company_address', 'company_bank_number', 'company_specialization']
        widgets = {
            'company_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите код компании'}),
            'company_full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите полное наименование'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите краткое наименование'}),
            'company_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите адрес компании'}),
            'company_bank_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер банка'}),
            'company_specialization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите специализацию'}),
        }


class DeleteCompany(forms.Form):
    company_id = forms.IntegerField(label="ID компании")
    company_id  = forms.ModelChoiceField(
        queryset=Company.objects.all(),  # Список существующих сотрудников
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="ID компании"
    )

    class Meta:
        model = Company
        fields = ['company_id']


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name', 'employee_age', 'company']
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя сотрудника'}),
            'employee_age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите возраст'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
        }


class UpdateEmployeeForm(forms.ModelForm):
    employee_id = forms.ModelChoiceField(
        queryset=Employee.objects.all(),  # Список существующих сотрудников
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="ID сотрудника"
    )

    class Meta:
        model = Employee
        fields = ['employee_id','employee_name', 'employee_age', 'company']
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя сотрудника'}),
            'employee_age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите возраст'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
        }


class DeleteEmployeeForm(forms.ModelForm):
    employee_id = forms.ModelChoiceField(
        queryset=Employee.objects.all(),  # Список существующих сотрудников
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="ID сотрудника"
    )

    class Meta:
        model = Employee
        fields = ['employee_id']  


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'employee']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название категории'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
        }


class AddAgreementForm(forms.ModelForm):
    class Meta:
        model = Agreement
        fields = ['agreement_start_date', 'agreement_end_date', 'agreement_total_payments', 'agent']
        widgets = {
            'agreement_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'agreement_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'agreement_total_payments': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите общую сумму платежей'}),
            'agent': forms.Select(attrs={'class': 'form-control'}),
        }

class AddCategoryPayment(forms.ModelForm):
    class Meta:
        model = CategoryPayment
        fields = ['payment_amount', 'category', 'agreement']
        widgets = {
            'payment_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите сумму выплат'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'agreement': forms.Select(attrs={'class': 'form-control'}),
        }


class AddEmployeeToAgreement(forms.ModelForm):
    class Meta:
        model = EmployeeToAgreement
        fields = ['employee', 'agreement']
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'agreement': forms.Select(attrs={'class': 'form-control'}),
        }


class Search1(forms.Form):
    company_id = forms.ModelChoiceField(
        queryset=Company.objects.all(),  # Список существующих компаний
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='ID компании'
    )
    selected_date = forms.DateField(
        label='Date',
        widget=forms.SelectDateWidget(attrs={'class': 'form-control'}),
        required=True
    )

class Search3(forms.Form):
    selected_date = forms.DateField(
        label='Date',
        widget=forms.SelectDateWidget(attrs={'class': 'form-control'}),
        required=True
    )