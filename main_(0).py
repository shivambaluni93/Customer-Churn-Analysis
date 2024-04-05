

import streamlit as st
import pickle
import pandas as pd

# Load the saved Random Forest model
model_filename = 'random_forest.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Function to predict churn
def predict_churn(data):
    prediction = model.predict(data)
    return prediction[0]

# Streamlit app
st.title("Churn Classification App")

# Input features
area_code = st.selectbox("Area Code", [415, 408, 510])
account_length = st.slider("Account Length", min_value=1, max_value=243, step=1, value=100)
voice_plan = st.selectbox("Voice Plan", ['No', 'Yes'])
voice_messages = st.slider("Voice Messages", min_value=0, max_value=60, step=1, value=20)
intl_plan = st.selectbox("International Plan", ['No', 'Yes'])
intl_mins = st.slider("International Minutes", min_value=0, max_value=20, step=1, value=10)
intl_calls = st.slider("International Calls", min_value=0, max_value=20, step=1, value=5)
intl_charge = st.slider("International Charge", min_value=0, max_value=50, step=1, value=10)
day_mins = st.slider("Day Minutes", min_value=0, max_value=300, step=1, value=150)
day_calls = st.slider("Day Calls", min_value=0, max_value=160, step=1, value=75)
day_charge = st.slider("Day Charge", min_value=0, max_value=60, step=1, value=30)
eve_mins = st.slider("Evening Minutes", min_value=0, max_value=300, step=1, value=150)
eve_calls = st.slider("Evening Calls", min_value=0, max_value=160, step=1, value=75)
eve_charge = st.slider("Evening Charge", min_value=0, max_value=30, step=1, value=15)
night_mins = st.slider("Night Minutes", min_value=0, max_value=300, step=1, value=150)
night_calls = st.slider("Night Calls", min_value=0, max_value=160, step=1, value=75)
night_charge = st.slider("Night Charge", min_value=0, max_value=15, step=1, value=7)
customer_calls = st.slider("Customer Calls", min_value=0, max_value=20, step=1, value=5)

# Create a DataFrame with the input features
input_data = pd.DataFrame({
    'Area_Code': [area_code],
    'Account_Length': [account_length],
    'Voice_Plan': [1 if voice_plan == 'Yes' else 0],
    'Voice_Messages': [voice_messages],
    'Intl_Plan': [1 if intl_plan == 'Yes' else 0],
    'Intl_Mins': [intl_mins],
    'Intl_Calls': [intl_calls],
    'Intl_Charge': [intl_charge],
    'Day_Mins': [day_mins],
    'Day_Calls': [day_calls],
    'Day_Charge': [day_charge],
    'Eve_Mins': [eve_mins],
    'Eve_Calls': [eve_calls],
    'Eve_Charge': [eve_charge],
    'Night_Mins': [night_mins],
    'Night_Calls': [night_calls],
    'Night_Charge': [night_charge],
    'Customer_Calls': [customer_calls]
})

# Predict and display result
if st.button("Predict Churn"):
    result = predict_churn(input_data)
    st.success(f"The predicted churn is {result}")
