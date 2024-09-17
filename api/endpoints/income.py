from uuid import UUID
from fastapi import APIRouter, Depends, status
from api.services.income import IncomeService
from api.interfaces.income import IncomeRead, IncomeCreate, IncomeUpdate
from api.interfaces.utils import List

income_router = APIRouter(prefix="/incomes")


@income_router.get("/{income_id}", response_model=IncomeRead)
async def get_income(income_id: UUID, service: IncomeService = Depends(IncomeService)):
    return await service.get_income(income_id)


@income_router.get("", response_model=List[IncomeRead])
async def get_incomes(service: IncomeService = Depends(IncomeService)):
    return await service.get_incomes()


@income_router.post("", status_code=status.HTTP_201_CREATED, response_model=IncomeRead)
async def create_income(info: IncomeCreate, service: IncomeService = Depends(IncomeService)):
    return await service.create_income(info)


@income_router.patch("/{income_id}", response_model=IncomeRead)
async def update_income(income_id: UUID, info: IncomeUpdate, service: IncomeService = Depends(IncomeService)):
    return await service.update_income(income_id, info)


@income_router.delete("/{income_id}")
async def delete_income(income_id: UUID, service: IncomeService = Depends(IncomeService)):
    await service.delete_income(income_id)
