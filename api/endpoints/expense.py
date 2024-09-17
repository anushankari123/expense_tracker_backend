from uuid import UUID
from fastapi import APIRouter, Depends, status
from api.services.expense import ExpenseService
from api.interfaces.expense import ExpenseRead, ExpenseCreate, ExpenseUpdate
from api.interfaces.utils import List

expense_router = APIRouter(prefix="/expenses")

@expense_router.get("/{expense_id}", response_model=ExpenseRead)
async def get_expense(expense_id: UUID, service: ExpenseService = Depends(ExpenseService)):
    return await service.get_expense(expense_id)

@expense_router.get("", response_model=List[ExpenseRead])
async def get_expenses(service: ExpenseService = Depends(ExpenseService)):
    return await service.get_expenses()

@expense_router.post("", status_code=status.HTTP_201_CREATED, response_model=ExpenseRead)
async def create_expense(info: ExpenseCreate, service: ExpenseService = Depends(ExpenseService)):
    return await service.create_expense(info)

@expense_router.patch("/{expense_id}", response_model=ExpenseRead)
async def update_expense(expense_id: UUID, info: ExpenseUpdate, service: ExpenseService = Depends(ExpenseService)):
    return await service.update_expense(expense_id, info)

@expense_router.delete("/{expense_id}")
async def delete_expense(expense_id: UUID, service: ExpenseService = Depends(ExpenseService)):
    await service.delete_expense(expense_id)
