from pydantic import Field, PositiveFloat
from workout_API.contrib.schema import BaseSchema
from typing import Annotated

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description = 'Nome do Atleta', example = 'João', max_length = 50)]
    cpf: Annotated[str, Field(description = 'CPF do Atleta', example = '12345678900', max_length = 11)]
    idade: Annotated[str, Field(description = 'Idade do Atleta', example = '25')]
    peso: Annotated[PositiveFloat, Field(description = 'Peso do Atleta', example = '75.3')]
    altura: Annotated[PositiveFloat, Field(description = 'Altura do Atleta', example = '1.73')]
    sexo: Annotated[str, Field(description = 'Sexo do Atleta', example = 'M')]
