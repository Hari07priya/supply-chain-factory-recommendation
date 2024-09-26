import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

# Load the dataset from the CSV file
file_path = 'supplier_dataset.csv'
data = pd.read_csv(file_path)

# Prepare the dataset for training
X = data[['Supplier Rating', 'Delivery Performance', 'Communication', 'Price Competitiveness']]
y = data['Supplier Rating']  # Using 'Supplier Rating' as a proxy for the target score; adjust as needed

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Gradient Boosting Regressor
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

def recommend_factory(user_country, user_rating, user_delivery, user_communication, user_price, data, model):
    relevant_data = data[data['Country'] == user_country].copy()  # Create a copy of relevant data
    if relevant_data.empty:
        return None, "No data available for the specified country."  # Return None if no data available for the country

    # Predict the scores using the trained model
    relevant_data['Predicted Score'] = model.predict(relevant_data[['Supplier Rating', 'Delivery Performance', 'Communication', 'Price Competitiveness']])

    best_supplier = relevant_data.sort_values(by='Predicted Score', ascending=False).iloc[0]
    return best_supplier['Supplier ID'], best_supplier['Factory Name'], f"This supplier has the highest predicted score ({best_supplier['Predicted Score']}) based on your preferences."
