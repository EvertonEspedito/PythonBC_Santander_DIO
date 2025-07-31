from workout_API.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_collumn, relationship # type: ignore
from sqlalchemy.orm import Integer, String # type: ignore

class CategoriaModel(BaseModel):
    __tablename__ = 'Categorias'
    pk_id: Mapped[int] = mapped_collumn(Integer, primary_key = True)
    nome: Mapped[str] = mapped_collumn(String(50),unique = True, nullable = False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates= 'categoria')