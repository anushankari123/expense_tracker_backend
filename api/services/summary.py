from uuid import UUID
from typing import List
from datetime import date
from api.db.models.income import Income
from api.db.models.expense import Expense
from api.interfaces.income import IncomeRead
from api.interfaces.expense import ExpenseRead
from .base import BaseService

class SummaryService(BaseService):
    async def get_total_income(self, user_id: UUID) -> int:
        res = await Income.get(db=self.db, filters=[Income.user_id == user_id, ~Income.is_deleted])
        incomes = res.all()
        return sum(income.amount for income in incomes)

    async def get_total_expenses(self, user_id: UUID) -> int:
        res = await Expense.get(db=self.db, filters=[Expense.user_id == user_id, ~Expense.is_deleted])
        expenses = res.all()
        return sum(expense.amount for expense in expenses)

    async def get_expenses_by_date_range(self, user_id: UUID, start_date: date, end_date: date) -> List[ExpenseRead]:
        res = await Expense.get(db=self.db, filters=[Expense.user_id == user_id, ~Expense.is_deleted,
                                                     Expense.expense_date >= start_date,
                                                     Expense.expense_date <= end_date])
        return {"data": res.all()}

    async def get_summary(self, user_id: UUID, start_date: date, end_date: date):
        total_income = await self.get_total_income(user_id)
        total_expenses = await self.get_total_expenses(user_id)
        expenses = await self.get_expenses_by_date_range(user_id, start_date, end_date)
        return {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "expenses": expenses
        }
