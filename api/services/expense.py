from uuid import UUID
from sqlmodel import col
from api.db.models.expense import Expense
from api.interfaces.utils import List
from api.interfaces.expense import ExpenseRead, ExpenseCreate, ExpenseUpdate
from api.utils.exceptions import NotFoundError
from .base import BaseService

class ExpenseService(BaseService):
    async def get_expense(self, expense_id: UUID) -> ExpenseRead:
        """
        Retrieve a specific expense entry by its UUID.

        Args:
        - expense_id (UUID): The UUID of the expense entry to retrieve.

        Returns:
        - ExpenseRead: Details of the retrieved expense entry.

        Raises:
        - NotFoundError: Raised if the expense entry is not found.
        """
        res = await Expense.get(db=self.db, filters=[Expense.id == expense_id, ~col(Expense.is_deleted)])
        expense = res.one_or_none()
        if expense is None:
            raise NotFoundError("Expense entry not found")
        return expense

    async def get_expenses(self) -> List[ExpenseRead]:
        """
        Retrieve a list of non-deleted expense entries.

        Returns:
        - List[ExpenseRead]: List of non-deleted expense entries.
        """
        res = await Expense.get(db=self.db, filters=[~col(Expense.is_deleted)])
        return {"data": res.all()}

    async def create_expense(self, data: ExpenseCreate) -> ExpenseRead:
        """
        Create a new expense entry.

        Args:
        - data (ExpenseCreate): Information to create the expense entry.

        Returns:
        - ExpenseRead: Details of the created expense entry.
        
        Raises:
        - DuplicateConstraint: Raised if an expense entry with the same unique constraints already exists.
        """
        new_expense = Expense(**data.model_dump())
        await new_expense.save(self.db)
        return new_expense

    async def delete_expense(self, expense_id: UUID):
        """
        Mark an expense entry as deleted.

        Args:
        - expense_id (UUID): The UUID of the expense entry to delete.
        """
        expense = await self.get_expense(expense_id)
        expense.is_deleted = True
        await expense.save(self.db)

    async def update_expense(self, expense_id: UUID, data: ExpenseUpdate) -> ExpenseRead:
        """
        Update details of an expense entry.

        Args:
        - expense_id (UUID): The UUID of the expense entry to update.
        - data (ExpenseUpdate): Information to update the expense entry.

        Returns:
        - ExpenseRead: Details of the updated expense entry.
        
        Raises:
        - DuplicateConstraint: Raised if an expense entry with the same unique constraints already exists.
        """
        expense = await self.get_expense(expense_id)
        await expense.update(self.db, data)
        return expense
