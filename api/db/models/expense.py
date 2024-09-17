from sqlmodel import Field, SQLModel, AutoString
from uuid import UUID
from datetime import date
from .base import IdMixin, TimestampMixin, SoftDeleteMixin, BaseModel

class ExpenseBase(SQLModel):
    amount: int = Field(..., description="Expense amount")
    category: str = Field(..., description="Category of the expense", sa_type=AutoString)
    expense_date: date = Field(..., description="Date of the expense")
    user_id: UUID = Field(..., description="User ID to whom the expense belongs")

class Expense(BaseModel, ExpenseBase, IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    __tablename__ = "expenses"

    def __repr__(self):
        return f"<Expense (id: {self.id}, amount: {self.amount}, category: {self.category})>"
