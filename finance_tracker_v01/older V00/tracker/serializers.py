from rest_framework import serializers
from .models import Transaction, Budget, SavingdGoal

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'


class SavingdGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingdGoal
        fields = '__all__'