from rest_framework import viewsets
from .models import Transaction, Budget, SavingdGoal
from .serializers import TransactionSerializer, BudgetSerializer, SavingdGoalSerializer
from rest_framework.permissions import IsAuthenticated

class TransactionViewset(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
class SavingsGoalViewset(viewsets.ModelViewSet):
    serializer_class = SavingdGoalSerializer
    queryset = SavingdGoal.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
# Create your views here.
