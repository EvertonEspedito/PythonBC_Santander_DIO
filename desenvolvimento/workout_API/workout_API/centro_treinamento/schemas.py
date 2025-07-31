from workout_API.contrib.schema import BaseSchema


class CentroTreinamento(BaseSchema):
   nome: Annotated[str, Field(description = 'Nome do Centro de Treinamento', example = 'CT SAMURAI', max_length = 20)] # type: ignore
   endereco: Annotated[str, Field(description = 'Endereço do Centro de Treinamento', example = 'Rua x, Quadra 2, Cohab Massangano, Petrolina - PE', max_length = 60)] # type: ignore
   proprietario: Annotated[str, Field(description = 'Proprietario do Centro de Treinamento', example = 'João Paulo', max_length = 30)] # type: ignore