from uuid import UUID
from api.db.models.category import Category
from api.interfaces.category import CategoryRead, CategoryCreate, CategoryUpdate
from api.utils.exceptions import NotFoundError
from api.interfaces.utils import List
from .base import BaseService

class CategoryService(BaseService):
    async def get_category(self, category_id: UUID) -> CategoryRead:
        res = await Category.get(db=self.db, filters=[Category.id == category_id, ~Category.is_deleted])
        category = res.one_or_none()
        if category is None:
            raise NotFoundError("Category not found")
        return category

    async def get_categories(self) -> List[CategoryRead]:
        res = await Category.get(db=self.db, filters=[~Category.is_deleted])
        return {"data": res.all()}

    async def create_category(self, data: CategoryCreate) -> CategoryRead:
        new_category = Category(**data.model_dump())
        await new_category.save(self.db)
        return new_category

    async def delete_category(self, category_id: UUID):
        category = await self.get_category(category_id)
        category.is_deleted = True
        await category.save(self.db)

    async def update_category(self, category_id: UUID, data: CategoryUpdate) -> CategoryRead:
        category = await self.get_category(category_id)
        if data.name is not None:
            category.name = data.name
        await category.save(self.db)
        return category
