import pandas as pd
# import sys
# sys.path.append('../graphql_strawberry_fastapi')
# from schemas.poke_schema import Generation, Pokemon, PokeStats
# from preprocess_ds import refined_poke_data, refined_poke_desc_data
from .schemas.poke_schema import Generation, Pokemon, PokeStats
from .preprocess_ds import refined_poke_data, refined_poke_desc_data

__all__=[
    "process_pokedex"
]

class poke_data_transform:
    def __init__(self, **kwargs):
        self.poke_df = kwargs.get('ds')
        self.poke_desc_df = kwargs.get('ds2')
        self.poke_result_df = None

    def map_desc_data_to_poke_data(self):
        self.poke_df['japanese_name'] = None
        self.poke_df['classification'] = None
        self.poke_df['height_m'] = None
        self.poke_df['weight_kg'] = None

        for idx, row in self.poke_desc_df.iterrows():
            pokedex_num = row['pokedex_number']
            jap_name = row['japanese_name']
            class_poke = row['classfication']
            height_m = row['height_m']
            weight_kg = row['weight_kg']
            res_list = [jap_name, class_poke, height_m, weight_kg]
            self.poke_df.loc[self.poke_df['#'] == pokedex_num, 
                             'japanese_name':'weight_kg'] = res_list


    def set_region_name(self):
        generation_names=[]
        gen_names_dict={1: 'Kanto',
                        2: 'Johto',
                        3: 'Hoenn',
                        4: 'Sinnoh',
                        5: 'Unova',
                        6: 'Kalos',
                        7: 'Alola',
                        8: 'Galar'}

        for row in self.poke_df.iterrows():
            gen_num = row[1]['generation']
            if gen_num in gen_names_dict.keys():
                generation_names.append(gen_names_dict[gen_num])
        self.poke_df['gen_name'] = generation_names

    def add_points(self, column_name):
        points_column=[]
        for row in self.poke_df.iterrows():
            row_data=row[1]
            target_column=row_data[column_name]
            if not pd.isna(target_column):
                points_column.append(1)
            else:
                points_column.append(0)
        self.poke_df[f'{column_name}_points'] = points_column
    
        def agg_num_pokemon_region():
            pass

    def groupby_column(self, group_column_name, sum_column_name):
        grouped_df = self.poke_df.groupby([group_column_name])[sum_column_name].sum().reset_index()
        return grouped_df

def process_pie_chart():
    pass

def process_pokedex() -> Generation:
    poke_df=poke_df_obj.poke_df
    pokedex_data=[]
    print(poke_df.columns)
    for row in poke_df.iterrows():
        row_data=row[1]
        gen_name=row_data['gen_name']
        pokemon_name=row_data['name']
        japanese_name=row_data['japanese_name']
        pokedex_num=row_data['#']
        height=row_data['height_m']
        weight=row_data['weight_kg']
        type_1=row_data['type 1']
        type_2=row_data['type 2']
        hp=row_data['hp']
        attack=row_data['attack']
        defense=row_data['defense']
        sp_atk=row_data['sp. atk']
        sp_def=row_data['sp. def']
        speed=row_data['speed']

        pokedex_data.append(
        Pokemon(
            pokemon_name=pokemon_name,
            poke_japanese_name=japanese_name,
            pokedex_number=pokedex_num,
            stats_abilities=[PokeStats(
                hp=hp,
                attack=attack,
                defense=defense,
                sp_attack=sp_atk,
                sp_defense=sp_def,
                speed=speed
            
            )])
        )
    return (
        Generation(
        generation_name=gen_name,
        pokemon=pokedex_data
        )
    )


poke_df_obj=poke_data_transform(ds = refined_poke_data.df, 
                                ds2 = refined_poke_desc_data.df)
poke_df_obj.set_region_name()
poke_df_obj.map_desc_data_to_poke_data()
poke_df_obj.add_points('gen_name')
generation_groupby=poke_df_obj.groupby_column('gen_name', 'gen_name_points')
print(poke_df_obj.poke_df)
print(poke_df_obj.poke_df.columns)
# print(poke_df_obj.poke_result_df.columns)
# print(process_pokedex())
# print(type(process_pokedex()))

if __name__ == "__main__":
    # poke_df_obj=poke_data_transform('Pokemon_stats.csv')
    # poke_df_obj.set_region_name()
    # processed_pokedex=poke_df_obj.process_pokedex()
    # print(process_pokedex())
    # print(processed_pokedex)
    # print(type(processed_pokedex[0]))
    pass
