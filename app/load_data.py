import pandas as pd
import os

# poke_data_path = '/home/ra-terminal/datasets/Pokemon/Pokemon_stats.csv'
# poke_data = pd.read_csv(poke_data_path)
# print(poke_data.columns, len(list(poke_data.columns)))

# poke_desc_path = '/home/ra-terminal/datasets/Pokemon/pokemon_desc.csv'
# poke_desc_data = pd.read_csv(poke_desc_path)
# print(poke_desc_data.columns, len(list(poke_desc_data.columns)))

#---------------create json files

# poke_data.to_json('/home/ra-terminal/datasets/Pokemon/Pokemon_stats.json')
# poke_desc_data.to_json('/home/ra-terminal/datasets/Pokemon/pokemon_desc.json')

#--------------------

# poke_data_json_path = '/home/ra-terminal/datasets/Pokemon/Pokemon_stats.json'
# poke_data = pd.read_json(poke_data_json_path)
# print(poke_data.columns, len(list(poke_data.columns)))

# poke_desc_json_path = '/home/ra-terminal/datasets/Pokemon/pokemon_desc.json'
# poke_desc_data = pd.read_json(poke_desc_json_path)
# print(poke_desc_data.columns, len(list(poke_desc_data.columns)))

#-----------------------------------loading all data
class Load_Data:
    def __init__(self, **kwargs):
        self.dir_path = kwargs.get('path')
        self.chunk_size = kwargs.get('chunk_num')
        self.res_df = pd.DataFrame()

    def get_all_filepaths(self):
        #getting all files in dir that end in .json
        self.all_file_paths = [os.path.join(self.dir_path, f) for f in os.listdir(self.dir_path) if f.endswith('.json')]

    def get_dir_size(self):
        self.dir_size = len(self.all_file_paths)

    @staticmethod
    def process_data_in_chunks(all_file_paths, chunk_size):
        for i in range(0, len(all_file_paths), chunk_size):
            chunk_paths = all_file_paths[i : i + chunk_size]
            dfs = []
            for path in chunk_paths:
                try:
                    rec = pd.read_json(path, typ = 'series')
                    df = pd.DataFrame([rec])
                    dfs.append(df)
                except ValueError as e:
                    print(f"Error reading {path}: {e}")
            if dfs:
                chunk_df = pd.concat(dfs, ignore_index=True)
                yield chunk_df

    def read_data_in_chunks(self):
        try:
            print('Processing Data')
            for idx, chunk_df in enumerate(Load_Data.process_data_in_chunks(all_file_paths = 
                                                         self.all_file_paths, 
                                                        chunk_size = self.chunk_size)):
                self.res_df = pd.concat([self.res_df, chunk_df], ignore_index=True)
            print('Finished Processing Data')
        except ValueError as e:
            print(f"Error: {e}")
        pass

poke_stats_path = '/home/ra-terminal/datasets/Pokemon/new_data/pokemon_stats_data/'
poke_desc_path = '/home/ra-terminal/datasets/Pokemon/new_data/pokemon_desc_data/'

chunk_num = 50
poke_stat_obj = Load_Data(path = poke_stats_path, chunk_num=chunk_num)
poke_stat_obj.get_all_filepaths()
poke_stat_obj.get_dir_size()
poke_stat_obj.read_data_in_chunks()
poke_data = poke_stat_obj.res_df

poke_desc_obj = Load_Data(path = poke_desc_path, chunk_num=chunk_num)
poke_desc_obj.get_all_filepaths()
poke_desc_obj.get_dir_size()
poke_desc_obj.read_data_in_chunks()
poke_desc_data = poke_desc_obj.res_df

if __name__ == '__main__':
    # chunk_num = 40
    # poke_stat_obj = Load_Data(path = poke_stats_path, chunk_num=chunk_num)
    # poke_stat_obj.get_all_filepaths()
    # poke_stat_obj.get_dir_size()
    # poke_stat_obj.read_data_in_chunks()
    # print(poke_stat_obj.res_df)
    
    # poke_desc_obj = Load_Data(path = poke_desc_path, chunk_num=chunk_num)
    # poke_desc_obj.get_all_filepaths()
    # poke_desc_obj.get_dir_size()
    # poke_desc_obj.read_data_in_chunks()
    pass