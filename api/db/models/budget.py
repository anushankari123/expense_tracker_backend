from sqlmodel import Field, SQLModel, AutoString
from uuid import UUID
from .base import IdMixin, TimestampMixin, SoftDeleteMixin, BaseModel

class BudgetBase(SQLModel):
    amount: int = Field(..., description="Budget amount")
    category: str = Field(..., description="Category of the budget", sa_type=AutoString)

class Budget(BaseModel, BudgetBase, IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    __tablename__ = "budgets"

    def __repr__(self):
        return f"<Budget (id: {self.id}, amount: {self.amount}, category: {self.category})>"
