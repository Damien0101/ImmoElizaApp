#  House Price Predition 🤑

## 📜 Project Description
*This project aims to predict house prices using a machine learning model implemented through a Streamlit web application. The application allows users to input various property details and receive an estimated price for their house. The prediction model is built using CatBoostRegressor, a robust machine learning algorithm known for its efficiency in handling categorical features.*

[![N|Solid](house.jpeg "easter egg")](https://ih1.redbubble.net/image.1303800767.8302/raf,360x360,075,t,fafafa:ca443f4786.jpg)

***click on the image to make your first prediction...***

## 👀 Project Overview 

This project is designed to predict house prices by allowing users to input various property details through an intuitive web interface. The application leverages machine learning to provide accurate price estimations based on inputs such as locality, property type, number of bedrooms, living area, and more.

## 🤖 Sample Code 
```python
languages = {"en": "English", "fr": "French"}

language = st.sidebar.selectbox(
    "🌍 Language",
    list(languages.keys()),
    format_func=lambda lang: languages[lang],
)

source_link = {
    "en": "Show link to source code repository",
    "fr": "montrer le lien du repository",

```

## ⏱️ Project Timeline 

### 1. Project Setup and Data Collection

Set up the project environment and repository.

Collect and preprocess data for house price prediction.

### 2. Model Training and Evaluation

Train the CatBoostRegressor model with the preprocessed data.
    
Evaluate and fine-tune the model for optimal performance.

### 3. Streamlit Application Development

Build the Streamlit application interface with user input fields.
    
Integrate the trained model into the application for real-time predictions.

### 4. App Deployment with Render

Deploy the Streamlit application using Render.
    
Test and debug the deployed application to ensure functionality and accuracy.

## ⛓️ Project Directory Structure 

```plaintext
ImmoElizaApp/
│
├── catboost_info
│   └── <catboost files>
│
├── data
│   ├── dataset_for_encoder.pkl
│   └── final_dataset.json
│
├── encoder
│   ├── encoder.pkl
│   └── preprocess_input.py
│
├── model
│   ├── cleaning_train.py
│   └── model.cbm
│
├── app.py
├── requirements.txt
└── README.md
```
   

## 🔧  Installation

To run the app locally, follow these steps:

1. Clone the repository:

    
    ``` git clone https://github.com/servietsky0/ImmoElizaApp ```
    

2. Navigate into the cloned repository:

    
    ``` cd ./ImmoElizaApp ```


3. Install the necessary dependencies using pip:

    
    ``` pip install -r requirements.txt ```
    

4. Once you did all the these steps, type this commande in the terminal:

   ``` python3 main.py ```   
          or               
   ``` python main.py ```
    

Or you can just open your web browser and navigate to [https://price-prediction-elje.onrender.com/](https://price-prediction-elje.onrender.com) to use the app.


---
## 🎉 Have Fun!

*I trust you'll find joy in using my app, just as much joy as I had in developing it! Every input is a step towards a more accurate and insightful prediction of your house's value.* 🚀