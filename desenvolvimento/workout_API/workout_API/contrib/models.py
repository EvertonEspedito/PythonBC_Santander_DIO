from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_collumn
from sqlalchemy.orm import UUID
from  uuid import uuid4
from sqlalchemy.orm.dialects.postgresql import UUID as PG_UUID

class BaseModel(DeclarativeBase):
    id:Mapped[UUID] = mapped_collumn(PG_UUID(as_uuid = True), default = uuid4, nullable = False)
