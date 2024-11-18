from sqlalchemy import CheckConstraint, Column, DateTime, String, SMALLINT

from src.core.db import Base


from datetime import datetime

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Integer
from sqlalchemy.orm import mapped_column, Mapped


class Rate(Base):
    """."""

    date_rate: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=True,
        default=datetime.now
    )
    rate: Mapped[float] = Column(
        SMALLINT
    )



    def __repr__(self):
        return f"Rate: {self.date_rate} Rate: {self.rate}"
