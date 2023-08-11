import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.title("Mobile Phone Price Predictor")

rfmodel = pickle.load(open('model.pkl','rb'))
mobile_df = pickle.load(open("mobile.pkl",'rb'))
mobile = pd.DataFrame(mobile_df)


brand = st.selectbox("Select Mobile Brand",mobile['brand'].unique(),placeholder='Mobile Brand')

model = st.selectbox("Select Mobile Model",mobile[mobile['brand']==brand]['model'].unique(),placeholder='Mobile Model')

os = st.selectbox("Select Operating System",mobile['os'].unique())

proccessor = st.selectbox("Select Processor",mobile['processor_brand'].unique())

num_sim = st.selectbox("Select No. of Sim",mobile['num_sim'].unique())

network_type = st.selectbox("Select Network Type",mobile['network_type'].unique())

NFC = st.selectbox("NFC Supported",['Yes','No'])

num_cores = st.selectbox("Select No. of CPU cores",mobile['num_cores'].unique())

clock_speed = st.selectbox("Select Clock Speed",mobile['clock_speed'].unique())

ram_x = st.selectbox("Select RAM Variant",mobile['ram_x'].unique())

storage= st.selectbox("Select Storage",mobile['storage'].unique())

battery_cap = st.number_input("Enter Battery Capacity")

charging = st.selectbox("Enter Charging Speed",mobile['charging'].unique())

camera_first = st.selectbox("Select Primary Camera Resolution",mobile['camera_first'].unique())

camera_front = st.selectbox("Select Front Camera Resolution",mobile['camera_front'].unique())

if st.button("Predict Price"):
 if NFC == 'Yes':
  NFC = 1
 else:
  NFC = 0

 input_var = np.array([model,78.00,os,brand,num_sim ,network_type,NFC,proccessor,num_cores,clock_speed,ram_x,storage,battery_cap,charging,camera_first,camera_front])
 input_var = input_var.reshape(1,16)
 ans = rfmodel.predict(input_var)[0]
 st.header(round(np.exp(ans),0))