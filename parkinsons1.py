import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
#from sklearn.naive_bayes import GaussianNB

# Title and Description
st.title("Parkinson's Disease Prediction App")
st.write("This app predicts whether a patient has Parkinson's disease using a trained model.")

try:
    model1= pickle.load(open(r'D:\streamlit\env\Disease_prediction\parkinsons.pkl', 'rb'))
except FileNotFoundError:
    st.error("file not found")
except OSError as e:
    st.error("error : {e}")

st.header("Enter Patient Details")

try:
    feature_names = model1.feature_names_in_
except AttributeError:
    st.error("feature not found")
    st.stop()

st.write("feature select:")
inputs={}
for feature in feature_names:
    inputs[feature] = st.number_input(feature, value=0.0)

if st.button('predict'):
    feature = np.array([list(inputs.values())])
    try:
        prediction = model1.predict(feature)

        if prediction[0] == 1:
            st.success("You have Liver Disease")
        else:
            st.success("You dont have Liver Disease")
    except Exception as e:
        st.error(f"error :{e}")