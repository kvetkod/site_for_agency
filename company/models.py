# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agent(models.Model):
    agent_id = models.AutoField(primary_key=True)
    agent_name = models.CharField(max_length=255)
    agent_passport_id = models.CharField(max_length=50)
    agent_passport_number = models.CharField(max_length=50)
    agent_passport_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'agent'


class Agreement(models.Model):
    agreement_id = models.AutoField(primary_key=True)
    agreement_start_date = models.DateField()
    agreement_end_date = models.DateField()
    agreement_total_payments = models.FloatField()
    agent = models.ForeignKey(Agent, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement'



class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    employee = models.OneToOneField('Employee', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class CategoryPayment(models.Model):
    category_payment_id = models.AutoField(primary_key=True)
    payment_amount = models.FloatField()
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    agreement = models.ForeignKey(Agreement, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_payment'


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_number = models.IntegerField()
    company_full_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=255)
    company_bank_number = models.CharField(max_length=50)
    company_specialization = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'company'


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    employee_age = models.IntegerField()
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeToAgreement(models.Model):
    employee_to_agreement_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    agreement = models.ForeignKey(Agreement, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_to_agreement'