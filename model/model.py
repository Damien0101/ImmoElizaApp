import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from catboost import CatBoostRegressor

'''# Load the dataset
df = pd.read_csv('data/dataset.csv')
df = df.drop_duplicates()


# Define CatBoost model parameters
params: dict[str, float] = {
    'learning_rate': 0.0921459262053085,
    'depth': 10,
    'subsample': 0.617993504291168,
    'colsample_bylevel': 0.8692370930849208,
    'min_data_in_leaf': 84,
}

# Split the target variable (Price) and features
y: np.ndarray = np.array(df['Price']).reshape(-1, 1)
X: np.ndarray = np.array(df.drop(['Price'], axis=1))


# Split the data into training and test sets
X_train: np.ndarray
X_test: np.ndarray
y_train: np.ndarray
y_test: np.ndarray
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=86)


# Initialize and train the CatBoost model
model: CatBoostRegressor = CatBoostRegressor(**params, n_estimators=1000, loss_function='RMSE')
model.fit(X_train, y_train, verbose=100)
model.save_model('data/model.cbm')

# Print the model score and mean absolute error on the test set
print(model.score(X_test, y_test))
y_pred: np.ndarray = model.predict(X_test)
print(mean_absolute_error(y_test, y_pred))'''

model = CatBoostRegressor()

model = model.load_model('model/model.cbm', 'cbm')

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

print(list(input.values()))

# model.predict(list(input.values()))