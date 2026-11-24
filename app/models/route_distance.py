from datetime import timedelta
from decimal import Decimal

from sqlalchemy import Integer, ForeignKey, Numeric, Interval, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class RouteDistance(Base):
    __tablename__ = "route_distances"
    __table_args__ = (
        UniqueConstraint(
            "address_a_id",
            "address_b_id",
            name="uq_route_distances_addresses"
        ),
        CheckConstraint(
            "address_a_id != address_b_id",
            name="ck_route_distances_different_addresses"
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address_a_id: Mapped[int] = mapped_column(
        ForeignKey("addresses.id"),
        nullable=False
    )
    address_b_id: Mapped[int] = mapped_column(
            ForeignKey("addresses.id"),
            nullable=False
        )
    kms: Mapped[Decimal] = mapped_column(
        Numeric(8, 2),
        nullable=False
    )
    duration_60: Mapped[timedelta] = mapped_column(
        Interval,
        nullable=False
    )

    duration_80: Mapped[timedelta] = mapped_column(
        Interval,
        nullable=False
    )
