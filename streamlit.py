# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:30:27 2022

@author: matui
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
from scipy import stats
from matplotlib.axis import Axis


survival = pd.read_csv(r'C:\Users\matui\Downloads\survival.csv', sep=";")

################### LAYOUT & INTRO ###################

st.set_page_config(layout="wide")
st.title('Patient Survival Data')
st.write('Analysis of dead people')
st.sidebar.write('Ferdinand Leube')
st.sidebar.write('Edgar Tomé')
st.sidebar.write('Mathieu Jomain')
st.write('Dataset of ~ 80k rows')
st.text("")
st.text("")


################### Admit source/death - CROSSTAB #######################

#crosstab
st.write('Number of alive/dead people by admission source')
cross1 = pd.crosstab(survival['icu_admit_source'], survival['hospital_death'])
cross1 = cross1.rename(columns={0:'Nb alive', 1:'Nb dead'})
st.table(cross1)

################### gender/death - CROSSTAB #######################

#crosstab
st.write('Number of alive/dead people by gender')
cross2 = pd.crosstab(survival['gender'], survival['hospital_death'])
cross2 = cross2.rename(columns={0:'Nb alive', 1:'Nb dead'})
st.table(cross2)

################### ethnicity/death - CROSSTAB #######################

#crosstab
st.write('Number of alive/dead people by ethnicity')
cross3 = pd.crosstab(survival['ethnicity'], survival['hospital_death'])
cross3 = cross3.rename(columns={0:'Nb alive', 1:'Nb dead'})
st.table(cross3)

################### STATISTICS #######################
st.write('Statistics for heart rate by gender')
if st.checkbox('Show dataframe'):
        chart_data = (survival.groupby('gender')['d1_heartrate_max','d1_heartrate_min'].agg(['mean', 'max', 'min']))
        chart_data

st.write('Statistics for glucose rate by gender')
if st.checkbox('Show dataframe',1):
        chart_data2 = (survival.groupby('gender')['d1_glucose_max','d1_glucose_min'].agg(['mean', 'max', 'min']))
        chart_data2


################### IMAGE #######################
image = Image.open(r'C:\Users\matui\Downloads\cat.jpg')