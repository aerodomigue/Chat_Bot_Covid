import pickle
import pandas


def fit(dataframe: pandas.DataFrame):
    pkl_filename = "finalized_model.sav"
    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)
        print(pickle_model)
    return pickle_model.predict(dataframe)

