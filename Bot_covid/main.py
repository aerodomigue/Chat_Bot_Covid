import pickle



dfValue = [[1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,1,1]]
print(dfValue)

pkl_filename = "finalized_model.sav"
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)
    print(pickle_model)
Ypredict = pickle_model.predict(dfValue)

print(Ypredict)