from rest_framework import viewsets
from .serializers import AgentSerializer, CompanySerializer, EmployeeSerializer, AgreementS, EmployeeToAgreementS, CategoryPaymentS, CategoryS
from django.shortcuts import render, redirect
from .forms import AgentForm, UpdateAgentForm, DeleteAgentForm, AddCompany, UpdateCompany, DeleteCompany, AddEmployeeForm, UpdateEmployeeForm, DeleteEmployeeForm, AddCategoryForm, AddAgreementForm, AddCategoryPayment, AddEmployeeToAgreement, Search1, Search3
from django.db import connection, IntegrityError, DatabaseError
from django.contrib import messages
from .models import Company, Agent, Employee, Agreement, CategoryPayment, Category, EmployeeToAgreement


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AgreementViewSet(viewsets.ModelViewSet):
    queryset = Agreement.objects.all()
    serializer_class = AgreementS

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryS

class EmployeeToAgreementViewSet(viewsets.ModelViewSet):
    queryset = EmployeeToAgreement.objects.all()
    serializer_class = EmployeeToAgreementS

class CategoryRaymentsViewSet(viewsets.ModelViewSet):
    queryset = CategoryPayment.objects.all()
    serializer_class = CategoryPaymentS

def index(request):
    # Получение списка всех компаний из базы данных
    companies = Company.objects.all()
    return render(request, 'company/index.html', {'companies': companies})


def agents(request):
    agents = Agent.objects.all()
    return render(request, 'company/agents.html', {'agents': agents})

def employees(request):
    employees = Employee.objects.select_related('company') \
        .prefetch_related('employeetoagreement_set__agreement').all()
    return render(request, 'company/employees.html', {'employees': employees})

def companies(request):
    companies = Company.objects.all()
    return render(request, 'company/companies.html', {'companies': companies})

def agreements(request):
    agreements = Agreement.objects.select_related('agent').all()
    category_payments = CategoryPayment.objects.all()
    return render(request, 'company/agreements.html', {'agreements': agreements, 'payments': category_payments})

def add_agent_function(agent_name, passport_id, passport_number, passport_date):
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                CALL add_agent(%s, %s, %s, %s);
            """, [agent_name, passport_id, passport_number, passport_date])
        except Exception as e:
            # Если возникает ошибка, возвращаем ее текст для отображения
            raise IntegrityError(str(e))

def agent_create(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            agent_name = form.cleaned_data['agent_name']
            passport_id = form.cleaned_data['agent_passport_id']
            passport_number = form.cleaned_data['agent_passport_number']
            passport_date = form.cleaned_data['agent_passport_date']
            
            try:
                # Попытка добавить агента
                add_agent_function(agent_name, passport_id, passport_number, passport_date)
                # Перенаправляем на страницу после успешного добавления
                return redirect('agents')  # Замените на нужную страницу
            except IntegrityError as e:
                # Если возникает ошибка, добавляем сообщение
                messages.error(request, str(e))  # Отправляем сообщение об ошибке в шаблон

    else:
        form = AgentForm()

    return render(request, 'company/agent_create.html', {'form': form})

def update_agent(request):
    error_message = None  # Переменная для хранения ошибки

    if request.method == 'POST':
        form = UpdateAgentForm(request.POST)
        if form.is_valid():
            # Получаем данные из формы
            agent_id = form.cleaned_data['agent_id'].agent_id
            agent_name = form.cleaned_data['agent_name']
            agent_passport_id = form.cleaned_data['agent_passport_id']
            agent_passport_number = form.cleaned_data['agent_passport_number']
            agent_passport_date = form.cleaned_data['agent_passport_date']

            # Вызов функции update_agent через SQL-запрос
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        CALL update_agent(%s, %s, %s, %s, %s);
                    """, [agent_id, agent_name, agent_passport_id, agent_passport_number, agent_passport_date])

                # Перенаправляем пользователя после успешного обновления
                return redirect('agents')  # Замените 'success_url' на нужный URL после обновления

            except DatabaseError as e:
                # Если PostgreSQL выбросил исключение, обрабатываем его
                error_message = str(e)  # Получаем текст ошибки

    else:
        form = UpdateAgentForm()

    return render(request, 'company/update_agent.html', {'form': form, 'error_message': error_message})

def delete_agent_function(agent_id):
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                CALL delete_agent(%s);
            """, [agent_id])
        except Exception as e:
            # Возвращаем ошибку, если агент не найден
            raise IntegrityError(str(e))

def delete_agent(request):
    if request.method == 'POST':
        form = DeleteAgentForm(request.POST)
        if form.is_valid():
            agent_id = form.cleaned_data['agent_id'].agent_id
            
            try:
                # Попытка удалить агента
                delete_agent_function(agent_id)
                # Перенаправляем на страницу после успешного удаления
                return redirect('agents')  # Замените на нужную страницу
            except IntegrityError as e:
                # Если возникает ошибка, добавляем сообщение
                messages.error(request, str(e))  # Отправляем сообщение об ошибке в шаблон

    else:
        form = DeleteAgentForm()

    return render(request, 'company/delete_agent.html', {'form': form})


def create_company(request):
    if request.method == "POST":
        form = AddCompany(request.POST)
        if form.is_valid():
            company_number = form.cleaned_data['company_number']
            company_full_name = form.cleaned_data['company_full_name']
            company_name =form.cleaned_data['company_name']
            company_address = form.cleaned_data['company_address']
            company_bank_number = form.cleaned_data['company_bank_number']
            company_specialization = form.cleaned_data['company_specialization']

            with connection.cursor() as cursor:
                try:
                    cursor.execute("""
                        CALL add_company(%s, %s, %s, %s, %s, %s)""", [ company_number, company_full_name, company_name, company_address, company_bank_number, company_specialization])

                    return redirect('companies')
                
                except Exception as e:
                    # Возвращаем ошибку, если агент не найден
                    messages.error(request, str(e))
    else:
        form = AddCompany()

    return render(request, 'company/add_company.html', {'form': form})


def update_company(request):
    if request.method == "POST":
        form = UpdateCompany(request.POST)
        if form.is_valid():
            company_id = form.cleaned_data['company_id']
            company_number = form.cleaned_data['company_number']
            company_full_name = form.cleaned_data['company_full_name']
            company_name =form.cleaned_data['company_name']
            company_address = form.cleaned_data['company_address']
            company_bank_number = form.cleaned_data['company_bank_number']
            company_specialization = form.cleaned_data['company_specialization']

            with connection.cursor() as cursor:
                try:
                    cursor.execute("""
                        CALL update_company(%s, %s, %s, %s, %s, %s, %s)""", [company_id, company_number, company_full_name, company_name, company_address, company_bank_number, company_specialization])

                    return redirect('companies')
                
                except Exception as e:
                    # Возвращаем ошибку, если агент не найден
                    messages.error(request, str(e))
    else:
        form = UpdateCompany()

    return render(request, 'company/update_company.html', {'form': form})


def delete_company(request):
    if request.method == "POST":
        form = DeleteCompany(request.POST)
        if form.is_valid():
            company_id = form.cleaned_data['company_id'].company_id

            with connection.cursor() as cursor:
                try:
                    cursor.execute("""
                        CALL delete_company(%s)""", [company_id])

                    return redirect('companies')
                
                except Exception as e:
                    # Возвращаем ошибку, если агент не найден
                    messages.error(request, str(e))
    else:
        form = DeleteCompany()

    return render(request, 'company/delete_company.html', {'form': form})


def add_employee(request):
    if request.method == "POST":
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['employee_name']
            age = form.cleaned_data['employee_age']
            company = form.cleaned_data['company']
            if company == None:
                messages.error(request, "No companies")
            else:
                with connection.cursor() as cursor:
                        cursor.execute("""
                            CALL add_employee(%s, %s, %s)""", [name, age, company.company_id])

                        return redirect('employees')
    
    else:
        form = AddEmployeeForm()

    return render(request, 'company/add_employee.html', {'form': form})


def update_employee(request):
    if request.method == "POST":
        form = UpdateEmployeeForm(request.POST)
        
        # Проверка на валидность формы
        if form.is_valid():
            # Получаем данные из формы
            index = form.cleaned_data['employee_id'].employee_id
            name = form.cleaned_data['employee_name']
            age = form.cleaned_data['employee_age']
            company = form.cleaned_data['company']
            
            # Проверка на отсутствие выбора для company и agreement
            if not company:
                form.add_error('company', 'Это поле обязательно для выбора.')
                return render(request, 'company/update_employee.html', {'form': form})

            # Выполнение запроса, если все поля корректны
            with connection.cursor() as cursor:
                cursor.execute("""
                    CALL update_employee(%s, %s, %s, %s)""", [
                    index, name, age, 
                    company.company_id
                ])
                
                return redirect('employees')

    else:
        form = UpdateEmployeeForm()

    return render(request, 'company/update_employee.html', {'form': form})



def delete_employee(request):
    if request.method == "POST":
        form = DeleteEmployeeForm(request.POST)
        
        # Проверка на валидность формы
        if form.is_valid():
            # Получаем данные из формы
            index = form.cleaned_data['employee_id'].employee_id

            # Выполнение запроса, если все поля корректны
            with connection.cursor() as cursor:
                cursor.execute("""
                    CALL delete_employee(%s)""", [
                    index
                ])
                
                return redirect('employees')

    else:
        form = DeleteEmployeeForm()

    return render(request, 'company/delete_employee.html', {'form': form})


def add_category(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            employee = form.cleaned_data['employee'].employee_id
            if employee == None:
                messages.error(request, "Select employee")
            else :
                with connection.cursor() as cursor:
                        cursor.execute("""
                            CALL add_category(%s, %s)""", [ name, employee ])

                        return redirect('employees')

    else:
        form = AddCategoryForm()

    return render(request, 'company/add_category.html', {'form': form})


def add_agreement(request):
    agreement_id = None  # Изначально agreement_id пустое

    if request.method == "POST":
        form = AddAgreementForm(request.POST)
        if form.is_valid():
            # Получаем данные из формы
            agreement_start_date = form.cleaned_data['agreement_start_date']
            agreement_end_date = form.cleaned_data['agreement_end_date']
            agreement_total_payments = form.cleaned_data['agreement_total_payments']
            agent = form.cleaned_data['agent'].agent_id 
            
            # Вставляем данные в базу через функцию add_agreement
            with connection.cursor() as cursor:
                try:
                    cursor.execute("""
                        CALL add_agreement(%s, %s, %s, %s);
                    """, [agreement_start_date, agreement_end_date, agreement_total_payments, agent])
                    # Получаем ID нового договора
                    agreement_id = cursor.fetchone()[0]  # Присваиваем ID договора переменной

            # После того как договор создан, передаем ID в шаблон для добавления выплат
                    
                except Exception as e:
                    # Возвращаем ошибку, если агент не найден
                    messages.error(request, str(e))
                
                return redirect('agreements')
    else:
        form = AddAgreementForm()

    return render(request, 'company/add_agreement.html', {'form': form, 'agreement_id': agreement_id})


def add_category_payment(request):
    if request.method == "POST":
        form = AddCategoryPayment(request.POST)
        if form.is_valid():
            payment = form.cleaned_data['payment_amount']
            category = form.cleaned_data['category'].category_id
            agreement = form.cleaned_data['agreement'].agreement_id
            with connection.cursor() as cursor:
                    cursor.execute("""
                        CALL add_category_payment(%s, %s, %s)""", [payment, category, agreement])

                    return redirect('agreements')
    
    else:
        form = AddCategoryPayment()

    return render(request, 'company/add_category_payment.html', {'form': form})

def add_employee_to_agreement(request):
    if request.method == "POST":
        form = AddEmployeeToAgreement(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee'].employee_id
            agreement = form.cleaned_data['agreement'].agreement_id
            with connection.cursor() as cursor:
                    cursor.execute("""
                        CALL add_employee_to_agreement(%s, %s)""", [employee, agreement])

                    return redirect('agreements')
    
    else:
        form = AddEmployeeToAgreement()

    return render(request, 'company/add_employee_to_agreement.html', {'form': form})
    

def search1(request):
    results = []
    if request.method == 'POST':
        form = Search1(request.POST)
        if form.is_valid():
            company_id = form.cleaned_data['company_id'].company_id
            selected_date = form.cleaned_data['selected_date']

            with connection.cursor() as cursor:
                cursor.execute('''
                    SELECT company_name, company_address, agreement_number, agreement_start_date, agreement_end_date
                    FROM search1(%s, %s)
                ''', [company_id, selected_date])
                results = cursor.fetchall()
    else:
        form = Search1()

    return render(request, 'company/search1.html', {'form': form, 'results': results})



def search2(request):
    results = []
    if request.method == 'POST':
        form = Search1(request.POST)
        if form.is_valid():
            company_id = form.cleaned_data['company_id'].company_id
            selected_date = form.cleaned_data['selected_date']

            with connection.cursor() as cursor:
                cursor.execute('''
                    SELECT agreement_date, company_name, agent_name
                    FROM search2(%s, %s)
                ''', [company_id, selected_date])
                results = cursor.fetchall()
    else:
        form = Search1()

    return render(request, 'company/search2.html', {'form': form, 'results': results})


def search3(request):
    results = []
    if request.method == 'POST':
        form = Search3(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['selected_date']

            with connection.cursor() as cursor:
                cursor.execute('''
                    SELECT employee_name, employee_category, payment_amount
                    FROM search3(%s)
                ''', [selected_date])
                results = cursor.fetchall()
    else:
        form = Search3()

    return render(request, 'company/search3.html', {'form': form, 'results': results})