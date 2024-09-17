from sqlmodel import SQLModel
from typing import Optional
from pydantic import ConfigDict
from uuid import UUID
from api.db.models.category import CategoryBase
from api.db.models import IdMixin, TimestampMixin, SoftDeleteMixin

class CategoryCreate(CategoryBase):
    model_config = ConfigDict(extra="forbid")

class CategoryRead(CategoryBase, IdMixin, TimestampMixin):
    pass

class CategoryReadInternal(CategoryRead, SoftDeleteMixin):
    pass

class CategoryUpdate(SQLModel):
    name: Optional[str] = None
