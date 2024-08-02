import catboost
import pickle
import pandas as pd


encoder = pickle.load(open('encoder/encoder.pkl', 'rb'))

def preprocessed_input(input):
        pd_input =pd.DataFrame(input)
        X = pd_input[encoder.feature_names_in_]
        X = encoder.transform(X)
        preprocessed_input = pd.concat([pd_input,X],axis=1).drop(columns=['District','FloodingZone','PEB','StateOfBuilding','Kitchen', 'Region','SubtypeOfProperty','Province', 'TypeOfSale'])
        return preprocessed_input

# prediction = model.predict(preprocessed_dict)
# print(prediction)



