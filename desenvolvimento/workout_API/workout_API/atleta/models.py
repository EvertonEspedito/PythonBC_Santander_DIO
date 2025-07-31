from workout_API.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_collumn, relationship # type: ignore
from sqlalchemy.orm import Integer, String, Float,Datetime # type: ignore
from datetime import datetime

class AtletaModel(BaseModel):
    __tablename__ = 'Atletas'
    pk_id: Mapped[int] = mapped_collumn(Integer, primary_key = True)
    nome: Mapped[str] = mapped_collumn(String(50), nullable = False)
    cpf: Mapped[str] = mapped_collumn(String(11), nullable = False)
    idade: Mapped[int] = mapped_collumn(Integer, nullable = False)
    peso: Mapped[float] = mapped_collumn(Float, nullable = False)
    altura: Mapped[float] = mapped_collumn(Float, nullable = False)
    sexo: Mapped[str] = mapped_collumn(String(1), nullable = False)
    cread_at: Mapped[datetime] = mapped_collumn(Datetime, nullable = False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates= 'atleta')
    categoria_id = Mapped[int] = mapped_collumn(ForeignKey('categorias.pk_id'))
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates= 'atleta')
    centro_treinamento_id = Mapped[int] = mapped_collumn(ForeignKey('centro_treinamento.pk_id'))