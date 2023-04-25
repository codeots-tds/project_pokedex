from typing import List
from typing import Union, Optional
import strawberry

@strawberry.type
class PokeStats:
    hp: None or int or float #Union[float, None]
    attack:None or int or float #Union[float, None]
    defense: None or int or float # Union[float, None]
    sp_attack:None or int or float #Union[float, None]
    sp_defense: None or int or float #Union[float, None]
    speed:None or int or float #Union[float, None]

@strawberry.type
class Pokemon:
    pokemon_name: None or str #Union[str, None]
    poke_japanese_name: None or str # Union[str, None]
    pokedex_number: None or int # Union[int, None]
    # height_meters: None or str or float 
    # weight_kg: None or str or float
    # type1:None or str
    # type2:None or str
    # percentage_male: None or str or float
    # base_egg_steps:None or int
    # classification: None or str
    stats_abilities:List[PokeStats]

@strawberry.type
class Generation:
    generation_name: None or str # Union[str, None]
    pokemon: List[Pokemon]