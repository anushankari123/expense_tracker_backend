from uuid import UUID
from fastapi import APIRouter, Depends, status
from api.services.category import CategoryService
from api.interfaces.category import CategoryRead, CategoryCreate, CategoryUpdate
from api.interfaces.utils import List

category_router = APIRouter(prefix="/categories")

@category_router.get("/{category_id}", response_model=CategoryRead)
async def get_category(category_id: UUID, service: CategoryService = Depends(CategoryService)):
    return await service.get_category(category_id)

@category_router.get("", response_model=List[CategoryRead])
async def get_categories(service: CategoryService = Depends(CategoryService)):
    return await service.get_categories()

@category_router.post("", status_code=status.HTTP_201_CREATED, response_model=CategoryRead)
async def create_category(info: CategoryCreate, service: CategoryService = Depends(CategoryService)):
    return await service.create_category(info)

@category_router.patch("/{category_id}", response_model=CategoryRead)
async def update_category(category_id: UUID, info: CategoryUpdate, service: CategoryService = Depends(CategoryService)):
    return await service.update_category(category_id, info)

@category_router.delete("/{category_id}")
async def delete_category(category_id: UUID, service: CategoryService = Depends(CategoryService)):
    await service.delete_category(category_id)
