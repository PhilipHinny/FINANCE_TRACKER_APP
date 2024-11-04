from django.contrib.auth.models import User
from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPES = (('income', 'Income'), ('expense', 'Expense'))
    User = models.ForeignKey( User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    transaction_types =models.CharField(choices=TRANSACTION_TYPES, max_length=10)
    date = models.DateField()

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=60)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()

class SavingdGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=100)
    Target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    saved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()

# Create your models here.
