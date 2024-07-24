import streamlit as st
import numpy as np
import joblib
from keras.models import load_model
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

model = load_model('water_quality_model.h5')
scaler = joblib.load('scaler.pkl')

st.title('Water Quality Prediction')
st.markdown('---')

data = pd.read_csv('waterQuality1.csv')

aluminium = st.sidebar.slider('Aluminium', min_value=0.0, max_value=10.0, value=1.65, step=0.01)
ammonia = st.sidebar.slider('Ammonia', min_value=0.0, max_value=25.0, value=9.08, step=0.01)
arsenic = st.sidebar.slider('Arsenic', min_value=0.0, max_value=10.0, value=0.04, step=0.01)
barium = st.sidebar.slider('Barium', min_value=0.0, max_value=10.0, value=2.85, step=0.01)
cadmium = st.sidebar.slider('Cadmium', min_value=0.0, max_value=10.0, value=0.007, step=0.001)
chloramine = st.sidebar.slider('Chloramine', min_value=0.0, max_value=10.0, value=0.35, step=0.01)
chromium = st.sidebar.slider('Chromium', min_value=0.0, max_value=10.0, value=0.83, step=0.01)
copper = st.sidebar.slider('Copper', min_value=0.0, max_value=10.0, value=0.17, step=0.01)
flouride = st.sidebar.slider('Flouride', min_value=0.0, max_value=10.0, value=0.05, step=0.01)
bacteria = st.sidebar.slider('Bacteria', min_value=0.0, max_value=10.0, value=0.2, step=0.01)
viruses = st.sidebar.slider('Viruses', min_value=0.0, max_value=10.0, value=0.0, step=0.01)
lead = st.sidebar.slider('Lead', min_value=0.0, max_value=10.0, value=0.054, step=0.01)
nitrates = st.sidebar.slider('Nitrates', min_value=0.0, max_value=50.0, value=16.08, step=0.1)
nitrites = st.sidebar.slider('Nitrites', min_value=0.0, max_value=10.0, value=1.13, step=0.01)
mercury = st.sidebar.slider('Mercury', min_value=0.0, max_value=10.0, value=0.007, step=0.001)
perchlorate = st.sidebar.slider('Perchlorate', min_value=0.0, max_value=100.0, value=37.75, step=0.1)
radium = st.sidebar.slider('Radium', min_value=0.0, max_value=10.0, value=6.78, step=0.01)
selenium = st.sidebar.slider('Selenium', min_value=0.0, max_value=10.0, value=0.08, step=0.01)
silver = st.sidebar.slider('Silver', min_value=0.0, max_value=10.0, value=0.34, step=0.01)
uranium = st.sidebar.slider('Uranium', min_value=0.0, max_value=10.0, value=0.02, step=0.01)

input_data = np.array([[aluminium, ammonia, arsenic, barium, cadmium, chloramine,
                        chromium, copper, flouride, bacteria, viruses, lead,
                        nitrates, nitrites, mercury, perchlorate, radium, selenium,
                        silver, uranium]])
input_data_scaled = scaler.transform(input_data)

prediction = model.predict(input_data_scaled)
prediction_class = 'safe' if prediction > 0.5 else 'unsafe'

st.markdown(f'<h4><span style="color:orange;">Prediction:</span> The water is {prediction_class}</h4>', unsafe_allow_html=True)
st.markdown(f'<h5><span style="color:orange;">Model Accuracy:</span> 94.5%</h5>', unsafe_allow_html=True)
st.markdown('---')
st.write('## Features Distribution')
features = ['Aluminium', 'Ammonia', 'Arsenic', 'Barium', 'Cadmium', 'Chloramine',
            'Chromium', 'Copper', 'Flouride', 'Bacteria', 'Viruses', 'Lead',
            'Nitrates', 'Nitrites', 'Mercury', 'Perchlorate', 'Radium', 'Selenium',
            'Silver', 'Uranium']
values = [aluminium, ammonia, arsenic, barium, cadmium, chloramine,
          chromium, copper, flouride, bacteria, viruses, lead,
          nitrates, nitrites, mercury, perchlorate, radium, selenium,
          silver, uranium]
st.bar_chart(pd.DataFrame({'Feature': features, 'Value': values}).set_index('Feature'))

st.markdown('---')

st.markdown('''
# **EDA Section**
---
''')

df = data
pr = ProfileReport(df, explorative=True)
st.header('**Input DataFrame**')
st.write(df)
st.write('---')
st.header('**Pandas Profiling Report**')
st_profile_report(pr)
