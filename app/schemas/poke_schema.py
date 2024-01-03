from typing import List, Optional, Union
import strawberry

@strawberry.type
class PokeStats:
    hp: Optional[int] = None
    attack: Optional[int] = None
    defense: Optional[int] = None
    sp_attack: Optional[int] = None
    sp_defense: Optional[int] = None
    speed: Optional[int] = None

@strawberry.type
class Pokemon:
    pokemon_name: Optional[str] = None
    poke_japanese_name: Optional[str] = None
    pokedex_number: Optional[int] = None
    # height_meters: Optional[Union[str, float]] = None
    # weight_kg: Optional[Union[str, float]] = None
    # type1: Optional[str] = None
    # type2: Optional[str] = None
    # percentage_male: Optional[Union[str, float]] = None
    # base_egg_steps: Optional[int] = None
    # classification: Optional[str] = None
    stats_abilities: List[PokeStats]

@strawberry.type
class Generation:
    generation_name: Optional[str] = None
    pokemon: List[Pokemon]