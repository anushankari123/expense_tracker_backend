from typing import Optional
from sqlmodel import SQLModel
from pydantic import ConfigDict
from uuid import UUID
from datetime import date
from api.db.models.income import IncomeBase
from api.db.models import IdMixin, TimestampMixin, SoftDeleteMixin


class IncomeCreate(IncomeBase):
    model_config = ConfigDict(extra="forbid")


class IncomeRead(IncomeBase, IdMixin, TimestampMixin):
    pass

class IncomeReadInternal(IncomeRead, SoftDeleteMixin):
    pass


class IncomeUpdate(SQLModel):
    amount: Optional[int] = None
    source: Optional[str] = None
    income_date: Optional[date] = None
    user_id: Optional[UUID]= None
