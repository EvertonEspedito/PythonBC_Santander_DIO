from workout_API.contrib.schema import BaseSchema
from typing import Annotated

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description = 'Nome do Atleta', exemples = 'João', max_length = 50)]
    cpf: Annotated[str, Field(description = 'CPF do Atleta', exemples = '12345678900', max_length = 11)]
    idade: Annotated[str, Field(description = 'Idade do Atleta', exemples = '25')]
    peso: Annotated[PositiveFloat, Field(description = 'Peso do Atleta', exemples = '75.3')]
    altura: Annotated[PositiveFloat, Field(description = 'Altura do Atleta', exemples = '1.73')]
    sexo: Annotated[str, Field(description = 'Sexo do Atleta', exemples = 'M')]
