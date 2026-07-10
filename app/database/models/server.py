from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from app.database.base import Base


class Server(Base):
    __tablename__ = "servers"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100))

    ip_address: Mapped[str] = mapped_column(String(50), unique=True)

    operating_system: Mapped[str] = mapped_column(String(50))

    status: Mapped[str] = mapped_column(String(20), default="offline")

    last_seen: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
