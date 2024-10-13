from sqlmodel import Field, SQLModel, AutoString
from uuid import UUID
from datetime import date
from .base import IdMixin, TimestampMixin, SoftDeleteMixin, BaseModel


class IncomeBase(SQLModel):
    amount: int = Field(..., description="Income amount")
    source: str = Field(..., description="Source of the income", sa_type=AutoString)
    income_date: date = Field(..., description="Date of income")
    

class Income(BaseModel ,IncomeBase, IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    __tablename__ = "incomes"

    def __repr__(self):
        return f"<Income (id: {self.id}, amount: {self.amount}, source: {self.source})>"
