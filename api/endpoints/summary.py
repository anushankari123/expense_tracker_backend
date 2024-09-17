from uuid import UUID
from datetime import date
from fastapi import APIRouter, Depends
from api.services.summary import SummaryService

summary_router = APIRouter(prefix="/summary")

@summary_router.get("/total-income/{user_id}")
async def get_total_income(user_id: UUID, service: SummaryService = Depends(SummaryService)):
    return await service.get_total_income(user_id)

@summary_router.get("/total-expenses/{user_id}")
async def get_total_expenses(user_id: UUID, service: SummaryService = Depends(SummaryService)):
    return await service.get_total_expenses(user_id)

@summary_router.get("/expenses/{user_id}")
async def get_expenses_by_date_range(user_id: UUID, start_date: date, end_date: date, service: SummaryService = Depends(SummaryService)):
    return await service.get_expenses_by_date_range(user_id, start_date, end_date)

@summary_router.get("/summary/{user_id}")
async def get_summary(user_id: UUID, start_date: date, end_date: date, service: SummaryService = Depends(SummaryService)):
    return await service.get_summary(user_id, start_date, end_date)
