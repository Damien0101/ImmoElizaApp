import streamlit as st
import pandas as pd 
import numpy as np
from catboost import CatBoostRegressor
from encoder.preprocess_input import preprocessed_input
import pickle

model = CatBoostRegressor()
model = model.load_model('model/model.cbm', 'cbm')

st.set_page_config(
page_title="Hangman",
page_icon="🏡",
)
 
languages = {"en": "English", "fr": "French"}

language = st.sidebar.selectbox(
    "🌍 Language",
    list(languages.keys()),
    format_func=lambda lang: languages[lang],
)

source_link = {
    "en": "Show link to source code repository",
    "fr": "montrer le lien du repository",
}

repo_url = "https://github.com/servietsky0/ImmoElizaApp"

info_hosting = {
    "en": f"Host your own app interface using <{repo_url}>",
    "fr": f"Hébergez votre propre interface application en utilisant <{repo_url}>",
}

if st.sidebar.checkbox(source_link[language]):
    st.info(info_hosting[language])

title_lang = {"en": "House Price Prediction 🏡", "fr": "Prédiction du prix des maisons 🏡"}

st.title(title_lang[language])

instruction = {
    "en": (
        "1. fill in the various fields based on the options.\n"
        "2. press the button to get the price of your house.\n"
        "3. Enjoy my app!"
    ),
    "fr": (
        "1. remplissez les différents champs sur base des options.\n"
        "2. appuyez sur le bouton pour obtenir le prix de votre maison.\n"
        "3. Amusez vous bien!"
    ),
}

st.write(instruction[language])


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
    st.success(f'{round(prediction(user_input)[0])}€')
    with st.expander("GET YOUR GIFT"):
            st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.F3bkgjbhmNNDPbwbDxAwKAAAAA%26pid%3DApi&f=1&ipt=1a57a25d2e9428e95a23d61f9a9424fc9231b4ca1961d2444bad565c3e3c2678&ipo=images")









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