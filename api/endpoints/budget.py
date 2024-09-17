from uuid import UUID
from fastapi import APIRouter, Depends, status
from api.services.budget import BudgetService
from api.interfaces.budget import BudgetRead, BudgetCreate, BudgetUpdate
from api.interfaces.utils import List

budget_router = APIRouter(prefix="/budgets")

@budget_router.get("/{budget_id}", response_model=BudgetRead)
async def get_budget(budget_id: UUID, service: BudgetService = Depends(BudgetService)):
    return await service.get_budget(budget_id)

@budget_router.get("", response_model=List[BudgetRead])
async def get_budgets(service: BudgetService = Depends(BudgetService)):
    return await service.get_budgets()

@budget_router.post("", status_code=status.HTTP_201_CREATED, response_model=BudgetRead)
async def create_budget(info: BudgetCreate, service: BudgetService = Depends(BudgetService)):
    return await service.create_budget(info)

@budget_router.patch("/{budget_id}", response_model=BudgetRead)
async def update_budget(budget_id: UUID, info: BudgetUpdate, service: BudgetService = Depends(BudgetService)):
    return await service.update_budget(budget_id, info)

@budget_router.delete("/{budget_id}")
async def delete_budget(budget_id: UUID, service: BudgetService = Depends(BudgetService)):
    await service.delete_budget(budget_id)
