from sqlalchemy import column
import streamlit as st
import pandas as pd 
import numpy as np
from catboost import CatBoostRegressor
from encoder.preprocess_input import preprocessed_input
import pickle

model = CatBoostRegressor()
model = model.load_model('model/model.cbm', 'cbm')

st.title('House Price Prediction 🏡')
st.write('Please enter the following details to get the prediction')


st.divider()
st.title('Type of Property ☯️')

TypeOfSale = st.selectbox('Type Of Sale', sorted(['Residential Sale', 'Residential Monthly Rent', 'Annuity Without Lump Sum',
 'Annuity Monthly Amount', 'Annuity Lump Sum']))

SubtypeOfProperty = st.selectbox('Subtype Of Property', sorted(['Flat Studio', 'House', 'Apartment', 'Villa', 'Apartment Block', 'Kot',
 'Ground Floor', 'Penthouse', 'Loft', 'Mixed Use Building', 'Duplex',
 'Town House', 'Service Flat', 'Mansion', 'Triplex', 'Exceptional Property',
 'Bungalow', 'Farmhouse', 'Country Cottage', 'Chalet', 'Manor House',
 'Other Property', 'Castle', 'Pavilion']))

TypeOfProperty = st.radio('Pick one:', ['Appartement','House'])
if TypeOfProperty == 'House':
    TypeOfProperty = 2
else:
    TypeOfProperty = 1


st.divider()
st.title('Locality 🌎')

District = st.selectbox('District', sorted(['Brugge', 'Veurne', 'Hasselt', 'Brussels', 'Nivelles', 'Mechelen',
 'Halle-Vilvoorde', 'Sint-Niklaas', 'Oostend', 'Antwerp', 'Ieper', 'Mons',
 'Namur', 'Philippeville', 'Leuven', 'Charleroi', 'Tournai', 'Liège', 'Maaseik',
 'Verviers', 'Aalst', 'Soignies', 'Tongeren', 'Marche-en-Famenne', 'Kortrijk',
 'Gent', 'Eeklo', 'Diksmuide', 'Dendermonde', 'Waremme', 'Huy', 'Oudenaarde',
 'Dinant', 'Neufchâteau', 'Mouscron', 'Tielt', 'Roeselare', 'Turnhout', 'Thuin',
 'Arlon', 'Virton', 'Ath', 'Bastogne']))

PostalCode = st.number_input('Postal Code', value=4020)

Province = st.selectbox('Province', sorted(['West Flanders', 'Limburg', 'Brussels', 'Walloon Brabant', 'Antwerp',
 'Flemish Brabant', 'East Flanders', 'Hainaut', 'Namur', 'Liège', 'Luxembourg']))

Region = st.selectbox('Region', sorted(['Wallonie' , 'Flanders', 'Brussels']))




st.divider()
st.title('Interior Of The House 🛋️')

BathroomCount = st.slider('Bathroom Count', min_value=0, max_value=4)

BedroomCount = st.slider('Bedroom Count', min_value=0, max_value=8)

ShowerCount = st.slider('ShowerCount', min_value=0, max_value=3)

ToiletCount = st.slider('Toilet Count', min_value=0, max_value=3)

LivingArea = st.number_input('Living Area' ,format="%f")

NumberOfFacades = st.slider('Number Of Facades', min_value=0, max_value=8)

Kitchen = st.selectbox('Kitchen', sorted(['Installed', 'Hyper Equipped', 'Semi Equipped', 'USA Installed',
 'Not Installed', 'USA Hyper Equipped', 'USA Semi Equipped', 'USA Uninstalled']))




st.divider()
st.title('Exterior Of The House 🌳')

GardenArea = st.number_input('Garden Area', format="%f")

SurfaceOfPlot = st.number_input('SurfaceOfPlot',format="%f")

Garden = st.checkbox('Garden')

Terrace = st.checkbox('Terrace')

SwimmingPool = st.checkbox('Swimming Pool')




st.divider()
st.title('State of building ✨')

StateOfBuilding = st.selectbox('State Of Building', sorted(['Good', 'To Be Done Up', 'As New', 'To Renovate', 'To Restore', 'Just Renovated']))

PEB = st.selectbox('PEB', ['A', 'B', 'C', 'D', 'E', 'F', 'G'])

FloodingZone = st.selectbox('Flooding Zone', sorted(['Non Flood Zone', 'Possible Flood Zone', 'Recognized Flood Zone', 
 'Circumscribed Waterside Zone', 'Possible N Circumscribed Flood Zone',
 'Recognized N Circumscribed Waterside Flood Zone',
 'Recognized N Circumscribed Flood Zone', 'Circumscribed Flood Zone',
 'Possible N Circumscribed Waterside Zone']))



with open('encoder/encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

with open('data/dataset_for_encoder.pkl', 'rb') as f:
    df = pickle.load(f)

col_to_encode = ['Kitchen', 'Province', 'TypeOfSale', 'FloodingZone', 'PEB', 'Region', 'SubtypeOfProperty', 'StateOfBuilding', 'District']

col=['BathroomCount', 'BedroomCount', 'District', 'FloodingZone', 'Garden',
        'GardenArea', 'Kitchen', 'LivingArea', 'NumberOfFacades', 'PEB',
        'PostalCode', 'Province', 'Region', 'ShowerCount',
        'StateOfBuilding', 'SubtypeOfProperty', 'SurfaceOfPlot', 'SwimmingPool',
        'Terrace', 'ToiletCount', 'TypeOfProperty', 'TypeOfSale']

features = [BathroomCount, BedroomCount, District, FloodingZone, Garden,
       GardenArea, Kitchen, LivingArea, NumberOfFacades, PEB,
       PostalCode, Province, Region, ShowerCount,
       StateOfBuilding, SubtypeOfProperty, SurfaceOfPlot, SwimmingPool,
       Terrace, ToiletCount, TypeOfProperty, TypeOfSale]

features = pd.DataFrame([features], columns=col)

 

ohetransform = encoder.transform(pd.DataFrame([col_to_encode], columns=col_to_encode))
user_input = pd.concat([features, ohetransform], axis=1).drop(columns=col_to_encode)


def prediction(features):   
    prediction = model.predict(features) 
    return prediction 

if st.button('Predict'):
    st.success(round(prediction(user_input)))










input ={"BathroomCount":4,
        "BedroomCount":2,
        "Garden":1,
        "GardenArea":650,
        "LivingArea":400,
        "NumberOfFacades":2,
        "PostalCode":4020,
        "ShowerCount":3,
        "SurfaceOfPlot":1100,
        "SwimmingPool":1,
        "Terrace":1,
        "ToiletCount":1,
        "TypeOfProperty":1,
        "District":'Liège',
        'FloodingZone':'NON_FLOOD_ZONE',
        'PEB':"A",
        'StateOfBuilding':"GOOD",
        'Kitchen':"",
        'Region':"Wallonie",
        'SubtypeOfProperty':'triplex',
        'Province':"Liège",
        'TypeOfSale':"residential_sale"}