from uuid import UUID
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, SQLModel, Relationship
from .base import IdMixin, TimestampMixin, SoftDeleteMixin, BaseModel

if TYPE_CHECKING:
    from .user import User


class LocationBase(SQLModel):
    name: str = Field(..., description="Name of the location", nullable=False)
    city: str = Field(..., description="City of the location", nullable=False)
    state: str = Field(..., description="State of the location", nullable=False)
    zip_code: str = Field(..., description="Zip code of the location", nullable=False)
    country: str = Field(..., description="Country of the location", nullable=False)
    address: str = Field(..., description="Enter the full address", nullable=False)
    latitude: Optional[float] = Field(None, description="Latitude of the location")
    longitude: Optional[float] = Field(None, description="Longitude of the location")


class Location(BaseModel, LocationBase, IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    __tablename__ = "locations"

    user_id: UUID = Field(default=None, foreign_key="users.id", ondelete="CASCADE")
    user: "User" = Relationship(back_populates="locations")

    def __repr__(self):
        return f"<Location (id: {self.id}, name: {self.name})>"
