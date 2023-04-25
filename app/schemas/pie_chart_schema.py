import strawberry
from typing import List, Union

@strawberry.type
class Num_Pokemon:
    pokemon_number: Union[int, None]

@strawberry.type
class GenPieChart:
    generation:Union[str, None]
    chart_data: List[Num_Pokemon]