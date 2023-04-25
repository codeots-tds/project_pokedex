import pandas as pd
from .load_data import poke_data, poke_desc_data

class Preprocess_DS:
    def __init__(self, **kwargs):
        self.df = kwargs.get('ds')

    def lower_headers(self):
        self.df.columns = self.df.columns.str.lower()

    def lower_str_col(self, col):
        self.df[col] = self.df[col].str.lower()

    def set_col_list_to_int(self, list_of_cols):
        self.df[list_of_cols] = self.df[list_of_cols].astype(int)


refined_poke_data = Preprocess_DS(ds = poke_data)
refined_poke_data.lower_headers()
refined_poke_data.lower_str_col(col = 'name')
poke_data_numeric_cols = refined_poke_data.df.select_dtypes(include=['int']).columns.tolist()
refined_poke_data.set_col_list_to_int(list_of_cols=poke_data_numeric_cols)
# refined_poke_data.

refined_poke_desc_data = Preprocess_DS(ds = poke_desc_data)
refined_poke_desc_data.lower_headers()
refined_poke_desc_data.lower_str_col(col = 'name')
# poke_data_desc_numeric_cols = refined_poke_desc_data.df.select_dtypes(include=['int']).columns.tolist()
# refined_poke_data.set_col_list_to_int(list_of_cols=poke_data_desc_numeric_cols)