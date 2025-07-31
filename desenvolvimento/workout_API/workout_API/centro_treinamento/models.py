from workout_API.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_collumn, relationship # type: ignore
from sqlalchemy.orm import Integer, String # type: ignore

class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centros_treinamento'
    pk_id: Mapped[int] = mapped_collumn(Integer, primary_key = True)
    nome: Mapped[str] = mapped_collumn(String(10), nullable = False)
    endereco: Mapped[str] = mapped_collumn(String(60), nullable = False)
    proprietario: Mapped[str] = mapped_collumn(String(30), nullable = False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates= 'centro_treinamento')