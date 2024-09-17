from uuid import UUID
from sqlmodel import col
from api.db.models.income import Income
from api.interfaces.utils import List
from api.interfaces.income import IncomeRead, IncomeCreate, IncomeUpdate
from api.utils.exceptions import NotFoundError
from .base import BaseService

class IncomeService(BaseService):
    async def get_income(self, income_id: UUID) -> IncomeRead:
        """
        Retrieve a specific income entry by its UUID.

        Args:
        - income_id (UUID): The UUID of the income entry to retrieve.

        Returns:
        - IncomeRead: Details of the retrieved income entry.

        Raises:
        - NotFoundError: Raised if the income entry is not found.
        """
        res = await Income.get(db=self.db, filters=[Income.id == income_id, ~col(Income.is_deleted)])
        income = res.one_or_none()
        if income is None:
            raise NotFoundError("Income entry not found")
        return income

    async def get_incomes(self) -> List[IncomeRead]:
        """
        Retrieve a list of non-deleted income entries.

        Returns:
        - List[IncomeRead]: List of non-deleted income entries.
        """
        res = await Income.get(db=self.db, filters=[~col(Income.is_deleted)])
        return {"data": res.all()}

    async def create_income(self, data: IncomeCreate) -> IncomeRead:
        """
        Create a new income entry.

        Args:
        - data (IncomeCreate): Information to create the income entry.

        Returns:
        - IncomeRead: Details of the created income entry.
        
        Raises:
        - DuplicateConstraint: Raised if an income entry with the same unique constraints already exists.
        """
        new_income = Income(**data.model_dump())
        await new_income.save(self.db)
        return new_income

    async def delete_income(self, income_id: UUID):
        """
        Mark an income entry as deleted.

        Args:
        - income_id (UUID): The UUID of the income entry to delete.
        """
        income = await self.get_income(income_id)
        income.is_deleted = True
        await income.save(self.db)

    async def update_income(self, income_id: UUID, data: IncomeUpdate) -> IncomeRead:
        """
        Update details of an income entry.

        Args:
        - income_id (UUID): The UUID of the income entry to update.
        - data (IncomeUpdate): Information to update the income entry.

        Returns:
        - IncomeRead: Details of the updated income entry.
        
        Raises:
        - DuplicateConstraint: Raised if an income entry with the same unique constraints already exists.
        """
        income = await self.get_income(income_id)
        await income.update(self.db, data)
        return income
