from sqlalchemy import String, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    company_name: Mapped[str] = mapped_column(String(255), nullable=False)
    address_type: Mapped[str] = mapped_column(String(50), nullable=False)
    street: Mapped[str] = mapped_column(String(150), nullable=False)
    building_number: Mapped[str] = mapped_column(String(20), nullable=False)
    apartment_number: Mapped[str | None] = mapped_column(String(20), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    notes: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    latitude: Mapped[float | None] = mapped_column(
        Numeric(9, 6),
        nullable=True
    )
    longitude: Mapped[float | None] = mapped_column(
        Numeric(9, 6),
        nullable=True
    )