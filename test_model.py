import pandas as pd
from catboost import CatBoostRegressor
import pickle

# Load the dataset, model, and encoder
df = pd.read_csv('data/dataset.csv')
model = CatBoostRegressor()
model.load_model('model/model.cbm', 'cbm')

with open('encoder/encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

# Input data
input_data = {
    "BathroomCount": 1,
    "BedroomCount": 2,
    "Garden": 1,
    "GardenArea": 2000,
    "LivingArea": 200,
    "NumberOfFacades": 4,
    "PostalCode": 3000,
    "ShowerCount": 1,
    "SurfaceOfPlot": 3000,
    "SwimmingPool": 0,
    "Terrace": 1,
    "ToiletCount": 2.2,
    "TypeOfProperty": 2,
    "District": 'Brussels',
    'FloodingZone': 'NON_FLOOD_ZONE',
    'PEB': "A",
    'StateOfBuilding': "GOOD",
    'Kitchen': "Equipped",
    'Region': "Wallonie",
    'SubtypeOfProperty': 'house',
    'Province': "Brussels",
    'TypeOfSale': "residential_sale"
}
# number of facades shouldn't be in the knn 

col_to_encode = ['Kitchen', 'Province', 'TypeOfSale', 'FloodingZone', 'PEB', 'Region', 'SubtypeOfProperty', 'StateOfBuilding', 'District']
col = ['BathroomCount', 'BedroomCount', 'District', 'FloodingZone', 'Garden', 'GardenArea', 'Kitchen', 'LivingArea', 'NumberOfFacades', 'PEB', 'PostalCode', 'Province', 'Region', 'ShowerCount', 'StateOfBuilding', 'SubtypeOfProperty', 'SurfaceOfPlot', 'SwimmingPool', 'Terrace', 'ToiletCount', 'TypeOfProperty', 'TypeOfSale']

features = pd.DataFrame([input_data])

encoded_features = encoder.transform(features[col_to_encode])
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(col_to_encode))


features = features.drop(columns=col_to_encode)
user_input = pd.concat([features, encoded_df], axis=1)


prediction = model.predict(user_input)


print(user_input)
print(prediction)
