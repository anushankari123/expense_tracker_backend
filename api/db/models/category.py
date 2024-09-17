from sqlmodel import Field, SQLModel, AutoString
from uuid import UUID
from .base import IdMixin, TimestampMixin, SoftDeleteMixin, BaseModel

class CategoryBase(SQLModel):
    name: str = Field(..., description="Category name", sa_type=AutoString)
    user_id: UUID = Field(..., description="User ID to whom the category belongs")

class Category(BaseModel, CategoryBase, IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    __tablename__ = "categories"

    def __repr__(self):
        return f"<Category (id: {self.id}, name: {self.name})>"
