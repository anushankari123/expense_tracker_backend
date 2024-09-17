from uuid import UUID
from sqlmodel import col
from api.db.models.budget import Budget
from api.interfaces.utils import List
from api.interfaces.budget import BudgetRead, BudgetCreate, BudgetUpdate
from api.utils.exceptions import NotFoundError
from .base import BaseService

class BudgetService(BaseService):
    async def get_budget(self, budget_id: UUID) -> BudgetRead:
        """
        Retrieve a specific budget entry by its UUID.

        Args:
        - budget_id (UUID): The UUID of the budget entry to retrieve.

        Returns:
        - BudgetRead: Details of the retrieved budget entry.

        Raises:
        - NotFoundError: Raised if the budget entry is not found.
        """
        res = await Budget.get(db=self.db, filters=[Budget.id == budget_id, ~col(Budget.is_deleted)])
        budget = res.one_or_none()
        if budget is None:
            raise NotFoundError("Budget entry not found")
        return budget

    async def get_budgets(self) -> List[BudgetRead]:
        """
        Retrieve a list of non-deleted budget entries.

        Returns:
        - List[BudgetRead]: List of non-deleted budget entries.
        """
        res = await Budget.get(db=self.db, filters=[~col(Budget.is_deleted)])
        return {"data": res.all()}

    async def create_budget(self, data: BudgetCreate) -> BudgetRead:
        """
        Create a new budget entry.

        Args:
        - data (BudgetCreate): Information to create the budget entry.

        Returns:
        - BudgetRead: Details of the created budget entry.
        
        Raises:
        - DuplicateConstraint: Raised if a budget entry with the same unique constraints already exists.
        """
        new_budget = Budget(**data.model_dump())
        await new_budget.save(self.db)
        return new_budget

    async def delete_budget(self, budget_id: UUID):
        """
        Mark a budget entry as deleted.

        Args:
        - budget_id (UUID): The UUID of the budget entry to delete.
        """
        budget = await self.get_budget(budget_id)
        budget.is_deleted = True
        await budget.save(self.db)

    async def update_budget(self, budget_id: UUID, data: BudgetUpdate) -> BudgetRead:
        """
        Update details of a budget entry.

        Args:
        - budget_id (UUID): The UUID of the budget entry to update.
        - data (BudgetUpdate): Information to update the budget entry.

        Returns:
        - BudgetRead: Details of the updated budget entry.
        
        Raises:
        - DuplicateConstraint: Raised if a budget entry with the same unique constraints already exists.
        """
        budget = await self.get_budget(budget_id)
        await budget.update(self.db, data)
        return budget
