
from workout_API.contrib.schema import BaseSchema


class Categoria(BaseSchema):
   nome: Annotated[str, Field(description = 'Nome da Categoria', example = 'Scale', max_length = 10)] # type: ignore