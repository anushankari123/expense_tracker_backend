from uuid import UUID
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, SQLModel, Relationship
from .enums import OrderStatus
from .base import IdMixin, TimestampMixin, SoftDeleteMixin, BaseModel

if TYPE_CHECKING:
    from .user import User
    from .location import Location
    from .review import Review
    from .payment import Payment
    from .driver_assignment import DriverAssignment


class OrderBase(SQLModel):
    pickup_location_id: UUID = Field(
        ..., description="Pickup location for the order", nullable=False, foreign_key="locations.id", ondelete="CASCADE"
    )
    delivery_location_id: UUID = Field(
        ...,
        description="Delivery location for the order",
        nullable=False,
        foreign_key="locations.id",
        ondelete="CASCADE",
    )
    description: Optional[str] = Field(None, description="Description of the order")
    estimated_amount: float = Field(..., description="Estimated amount for the order", nullable=False)
    status: OrderStatus = Field(
        default=OrderStatus.ORDER_PLACED, description="Current status of the order", nullable=False
    )

    # TODO: Add product info fields.


class Order(BaseModel, OrderBase, IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    __tablename__ = "orders"

    customer_id: UUID = Field(..., description="User id", nullable=False, foreign_key="users.id", ondelete="CASCADE")
    customer: "User" = Relationship(back_populates="orders")
    pickup: "Location" = Relationship(sa_relationship_kwargs={"foreign_keys": "Order.pickup_location_id"})
    delivery: "Location" = Relationship(sa_relationship_kwargs={"foreign_keys": "Order.delivery_location_id"})
    driver_assignments: list["DriverAssignment"] = Relationship(
        back_populates="order", sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )
    review: "Review" = Relationship(back_populates="order", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    payments: list["Payment"] = Relationship(
        back_populates="order", sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )

    def __repr__(self):
        return f"<Order (id: {self.id}, estimated_amount: {self.estimated_amount}, status: {self.status})>"
