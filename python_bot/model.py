import pickle
import pandas
from os import path as os_path

class model:
    def __init__(self):
        print(os_path.abspath(os_path.split(__file__)[0]))
        pkl_filename = "finalized_model.sav"
        with open(pkl_filename, 'rb') as file:
            self.pickle_model = pickle.load(file)

    def fit(self, dataframe: pandas.DataFrame):
        value = [dataframe["value"].values]
        return self.pickle_model.predict([dataframe["value"].values])

