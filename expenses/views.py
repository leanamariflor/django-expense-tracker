from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm

def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    total = sum(exp.amount for exp in expenses)
    return render(request, 'expenses/expense_list.html', {'expenses': expenses, 'total': total})

def add_expense(request):
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('expense_list')
    return render(request, 'expenses/expense_form.html', {'form': form})

def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    form = ExpenseForm(request.POST or None, instance=expense)
    if form.is_valid():
        form.save()
        return redirect('expense_list')
    return render(request, 'expenses/expense_form.html', {'form': form})

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expenses/expense_delete.html', {'expense': expense})
