import strawberry
from app.transform_data import process_pokedex
from app.schemas.poke_schema import Generation, Pokemon
from app.schemas.pie_chart_schema import GenPieChart, Num_Pokemon
from app.transform_data import generation_groupby
from typing import List, Optional

def get_pie_chart_data()-> GenPieChart:
    pie_chart_data=[]
    gen_pie=[]
    for idx, row in generation_groupby.iterrows():
        gen_name=row['gen_name']
        points=row['gen_name_points']
        pie_chart_data.append(Num_Pokemon(pokemon_number=points))
        gen_pie.append(
            GenPieChart(
        generation=gen_name,
        chart_data=Num_Pokemon(pokemon_number = points)
        )
        )
    # return (gen_pie)
    return (
    GenPieChart(
        generation=gen_name,
        chart_data=pie_chart_data
        )
)

@strawberry.input
class PokemonStatsFilter:
    min_hp: Optional[int] = None
    max_hp: Optional[int] = None
    min_atk: Optional[int] = None
    max_atk: Optional[int] = None
    min_def: Optional[int] = None
    max_def: Optional[int] = None
    min_sp_atk: Optional[int] = None
    max_sp_atk: Optional[int] = None
    min_sp_def: Optional[int] = None
    max_sp_def: Optional[int] = None
    min_speed: Optional[int] = None
    max_speed: Optional[int] = None


@strawberry.type
class Query:
    PokeDex: Generation = strawberry.field(resolver=process_pokedex)
    GenBreakDown : GenPieChart = strawberry.field(resolver=get_pie_chart_data)

    def __init__(self, **kwargs):
        pass
 

    def choose_pokemon(self, selected_pokemon):
        selected_pokemon = selected_pokemon.lower()
        if selected_pokemon != 'None':
            try:
                self.res_pokemon = [pokemon for pokemon in self.all_pokemon.pokemon 
                               if pokemon.pokemon_name == selected_pokemon]
            except ValueError as e:
                print(e)
                print(f"{selected_pokemon} cannot be found")
    
    @staticmethod
    def check_min_max(stats):
        min_val = None
        max_val = None
        if stats[0] > stats[1]:
            max_val = stats[0]
            min_val = stats[1]
        max_val = stats[1]
        min_val = stats[0]
        return max_val, min_val
    
    @strawberry.field
    def filter_pokemon(self, filters: Optional[PokemonStatsFilter] = None) -> List[Pokemon]:
        try:
            all_pokemon = process_pokedex()
            filtered_pokemon = []
            for idx, pokemon in enumerate(all_pokemon.pokemon):
                if filters:
                    if filters.min_hp and pokemon.stats_abilities[0].hp < filters.min_hp:
                        continue
                    if filters.max_hp and pokemon.stats_abilities[0].hp > filters.max_hp:
                        continue
                    if filters.min_atk and pokemon.stats_abilities[0].attack < filters.min_atk:
                        continue
                    if filters.max_atk and pokemon.stats_abilities[0].attack > filters.max_atk:
                        continue
                    if filters.min_def and pokemon.stats_abilities[0].defense < filters.min_def:
                        continue
                    if filters.max_def and pokemon.stats_abilities[0].defense > filters.max_def:
                        continue
                    if filters.min_sp_atk and pokemon.stats_abilities[0].sp_attack < filters.min_sp_atk:
                        continue
                    if filters.max_sp_atk and pokemon.stats_abilities[0].sp_attack > filters.max_sp_atk:
                        continue
                    if filters.min_sp_def and pokemon.stats_abilities[0].sp_defense < filters.min_sp_def:
                        continue
                    if filters.max_sp_def and pokemon.stats_abilities[0].sp_defense > filters.max_sp_def:
                        continue
                    if filters.min_speed and pokemon.stats_abilities[0].speed < filters.min_speed:
                        continue
                    if filters.max_speed and pokemon.stats_abilities[0].speed > filters.max_speed:
                        continue
                filtered_pokemon.append(pokemon)
            return filtered_pokemon
        except Exception as e:
            print(f"Error in filter_pokemon: {e}")
            return []

schema = strawberry.Schema(query=Query)

if __name__ == '__main__':
    filter_pokemon = Query()
    pass