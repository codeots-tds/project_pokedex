import strawberry
from app.transform_data import process_pokedex
from app.schemas.poke_schema import Generation
from app.schemas.pie_chart_schema import GenPieChart, Num_Pokemon
from app.transform_data import generation_groupby

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


@strawberry.type
class Query:
    PokeDex: Generation = strawberry.field(resolver=process_pokedex)
    GenBreakDown : GenPieChart = strawberry.field(resolver=get_pie_chart_data)

    def __init__(self, **kwargs):
        self.all_pokemon = process_pokedex()
        self.stat_dict_refs = {
            'hp' : 'hp',
            'atk': 'attack',
            'def': 'defense',
            'spatk': 'sp_attack',
            'spdef': 'sp_defense',
            'speed': 'speed',
        }

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
    
    def check_greater_less_than(val):
        pass

    def build_query(self, stat_dict):
        #maybe stat_dict can be a dict of dicts with min/max values
        len_stat_dict = len(stat_dict)
        poke_entry_temp_list = []
        if stat_dict != 'None':
            try:
                for key, stats in stat_dict.items():
                    if len(stats) == 2:
                        max_val, min_val = Query.check_min_max(stats)
                        for pokemon in self.all_pokemon.pokemon:
                            poke_data_value = getattr(pokemon.stats_abilities[0], self.stat_dict_refs[key])
                            if poke_data_value >= min_val and poke_data_value <= max_val:
                                if pokemon not in poke_entry_temp_list:
                                    poke_entry_temp_list.append(pokemon)
                    # elif len(stats) == 1:
            except ValueError as e:
                print("unfilterable")


schema = strawberry.Schema(query=Query)

if __name__ == '__main__':
    filter_pokemon = Query()
    # filter_pokemon.choose_pokemon(selected_pokemon = 'charizard')
    stat_test_dict = {
        'hp': [50, 90],
        'atk': [60],
        'def': [60],
        'spatk': [50, 80],
        'spdef': [20, 80]
    }
    filter_pokemon.build_query(stat_test_dict)
    pass