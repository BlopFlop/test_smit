from sqlalchemy import CheckConstraint, Column, String, BIGINT

from src.core.db import Base


class CargoModel(Base):
    """."""

    cargo_type = Column(
        String(100),
        CheckConstraint("LENGTH(name) <= 100", name="check_len_type"),
        unique=True,
        nullable=False,
        comment="Тип груза"
    )
    description = Column(
        String(256),
        nullable=True,
        comment=(
            "Описание, необязательное поле, текст; не менее одного символа;"
        ),
    )
    cost = Column(
        BIGINT,
        CheckConstraint("cost > 0", name="check_cost_positive"),
        nullable=False,
        comment="Стоимость груза, целочисленное поле; больше 0;",
    )

    def __repr__(self):
        return f"Cargo_type: {self.cargo_type}"
