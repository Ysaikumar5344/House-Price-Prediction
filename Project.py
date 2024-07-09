import streamlit as st
import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
import pickle

st.title("House Price Prediction")
model=pickle.load(open(r"lr.pkl","rb"))
SquareFeet=st.number_input("Enter the size of the house",min_value=1000,max_value=2999,step=50)
Bedrooms  = st.number_input("Enter the number of Bedrooms",min_value=1,max_value=4,step=1)
Bathrooms = st.number_input("Enter the number of Bathrooms",min_value=1,max_value=3,step=1)
Neighborhood = st.radio("Enter the Name of Neighborhood",['Rural','Suburb','Urban'])
neighbor=1 if Neighborhood=="Rural" else 2 if Neighborhood=="Suburb" else 3
YearBuilt = st.number_input("Enter the Year of Construction",min_value=1900,max_value=2030,step=1)

input_data=np.array([[SquareFeet],[Bedrooms],[Bathrooms],[neighbor],[YearBuilt]])
Price = model.predict([[SquareFeet,Bedrooms,Bathrooms,neighbor,YearBuilt]])
if st.button("Submit"):
  prediction=model.predict(input_data)
  st.write("The price for the flat with given details is RS.",Price)
