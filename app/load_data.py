import pandas as pd

poke_data_path = '/home/ra-terminal/datasets/Pokemon/Pokemon_stats.csv'
poke_data = pd.read_csv(poke_data_path)

poke_desc_path = '/home/ra-terminal/datasets/Pokemon/pokemon_desc.csv'
poke_desc_data = pd.read_csv(poke_desc_path)