from datetime import datetime, timezone
from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address_id: Mapped[int] = mapped_column(
        ForeignKey("addresses.id"),
        nullable=False
    )
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    contact_person: Mapped[str] = mapped_column(String(150), nullable=False)
    tax_id: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    payment_terms: Mapped[int] = mapped_column(Integer, nullable=False, default=45)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    notes: Mapped[str | None] = mapped_column(String(1000), nullable=True)