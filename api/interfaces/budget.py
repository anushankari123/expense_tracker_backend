from typing import Optional
from sqlmodel import SQLModel
from pydantic import ConfigDict
from uuid import UUID
from api.db.models.budget import BudgetBase
from api.db.models import IdMixin, TimestampMixin, SoftDeleteMixin

class BudgetCreate(BudgetBase):
    model_config = ConfigDict(extra="forbid")

class BudgetRead(BudgetBase, IdMixin, TimestampMixin):
    pass

class BudgetReadInternal(BudgetRead, SoftDeleteMixin):
    pass

class BudgetUpdate(SQLModel):
    amount: Optional[int] = None
    category: Optional[str] = None
    user_id: Optional[UUID] = None
