import pandas as pd
import os
from sklearn.tree import DecisionTreeRegressor

os.system('clear')

melbourne_model = DecisionTreeRegressor(random_state=1)

melbourne_path = 'Kaggle/arquivos_kaggle/melb_data.csv'

melbourne_data = pd.read_csv(melbourne_path)

melbourne_data = melbourne_data.dropna(axis=0)

melbourne_features = ['Rooms', 'Bathroom', 'Landsize',
                      'Lattitude', 'Longtitude']

y = melbourne_data.Price
X = melbourne_data[melbourne_features]

melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))

# print(X.describe())

# print(X.head())

# Mostra as colunas do DataFrame
# print(melbourne_data.columns)
