from typing import Optional
from sqlmodel import SQLModel
from pydantic import ConfigDict
from uuid import UUID
from datetime import date
from api.db.models.expense import ExpenseBase
from api.db.models import IdMixin, TimestampMixin, SoftDeleteMixin

class ExpenseCreate(ExpenseBase):
    model_config = ConfigDict(extra="forbid")

class ExpenseRead(ExpenseBase, IdMixin, TimestampMixin):
    pass

class ExpenseReadInternal(ExpenseRead, SoftDeleteMixin):
    pass

class ExpenseUpdate(SQLModel):
    amount: Optional[int] = None
    category: Optional[str] = None
    expense_date: Optional[date] = None
    user_id: Optional[UUID] = None
