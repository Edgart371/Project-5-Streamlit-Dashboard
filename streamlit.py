# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 17:14:17 2022

@author: leube
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
from scipy import stats
from matplotlib.axis import Axis

from sklearn.preprocessing import LabelEncoder

data = pd.read_csv(r"C:\Users\leube\Downloads\survival_rate_patients.csv")
survival = pd.DataFrame(data)

list_wanted_columns = ['patient_id', 'hospital_id', 'age', 'ethnicity', 'gender', 'height','icu_admit_source','weight','aids','cirrhosis', 'diabetes_mellitus','hepatic_failure', 'immunosuppression', 'leukemia', 'lymphoma','solid_tumor_with_metastasis','hospital_death','d1_heartrate_max', 'd1_heartrate_min','d1_glucose_max', 'd1_glucose_min']
columns = list(survival.columns)
unwanted = [x for x in columns if x not in list_wanted_columns]
for x in unwanted:
    del survival[f'{x}']
    
columns = list(survival.columns)
for x in survival.columns:
    survival.drop(survival[survival[x].isnull()].index, inplace = True)
    
    
conditions = [
    survival['age']<20,
    ((survival['age']>=20)&(survival['age']<30)),
    ((survival['age']>=30)&(survival['age']<40)),
    ((survival['age']>=40)&(survival['age']<50)),
    ((survival['age']>=50)&(survival['age']<60)),
    ((survival['age']>=60)&(survival['age']<70)),
    ((survival['age']>=70)&(survival['age']<80)),
    ((survival['age']>=80)&(survival['age']<90))
]

choices = ['10-20',
           '20-30',
          '30-40',
          '40-50',
          '50-60',
          '60-70',
          '70-80',
          '80-90']

survival['age_bins'] = np.select(conditions, choices, 'huge')

conditions2 = [
    survival['height']<140,
    ((survival['height']>=140)&(survival['height']<150)),
    ((survival['height']>=150)&(survival['height']<160)),
    ((survival['height']>=160)&(survival['height']<170)),
    ((survival['height']>=170)&(survival['height']<180)),
    ((survival['height']>=180)&(survival['height']<190)),
    ((survival['height']>=190)&(survival['height']<200))
]
choices2 = ['130-140',
           '140-150',
           '150-160',
           '160-170',
           '170-180',
           '180-190',
           '190-200']
survival['height_bins'] = np.select(conditions2, choices2, 'huge')


conditions3 = [
    survival['weight']<50,
    ((survival['weight']>=50)&(survival['weight']<70)),
    ((survival['weight']>=70)&(survival['weight']<90)),
    ((survival['weight']>=90)&(survival['weight']<110)),
    ((survival['weight']>=110)&(survival['weight']<130)),
    ((survival['weight']>=130)&(survival['weight']<150)),
    ((survival['weight']>=150)&(survival['weight']<170)),
    ((survival['weight']>=170)&(survival['weight']<190))
]
choices3 = ['30-50',
            '50-70',
            '70-90',
            '90-110',
            '110-130',
            '130-150',
            '150-170',
            '170-190']
survival['weight_bins'] = np.select(conditions3, choices3, 'huge')

survival['gender_encoded'] = LabelEncoder().fit_transform(survival.gender)


def age_pie_chart(sickness):  
    # code to create loop for input of streamlit user input
    chartone = survival[[f'{sickness}','age_bins','patient_id']]
    an = chartone.pivot_table(index=[f'{sickness}'], values=['patient_id'], columns=['age_bins'], aggfunc='count')
    an.reset_index(inplace=True)

    dataforchart = an.loc[an[f'{sickness}']==1].transpose()
    dataforchart.reset_index(inplace=True)
    
    values = dataforchart[1].sum()
    dataforchart.loc[(dataforchart[1]/values < 0.05),'age_bins']='other'
    dataforchart = dataforchart.groupby(by='age_bins').agg({1:'sum'})
    dataforchart.reset_index(inplace=True)
    dataforchart.loc[(dataforchart[1]== np.nan), 1] = 0
    
    #define data
    data = list(dataforchart[1])
    labels = list(dataforchart['age_bins'])
    explode = [0.1 for x in labels]


    #define Seaborn color palette to use
    colors = sns.color_palette('pastel')[0:9]

    #create pie chart
    plt.pie(data,explode = explode, colors = colors, autopct='%.0f%%')
    plt.legend(labels, bbox_to_anchor=(1.2, 1.0), loc='upper left')
    return plt.show()

def weight_pie_chart(sickness):  
    # code to create loop for input of streamlit user input
    chartone = survival[[f'{sickness}','weight_bins','patient_id']]
    an = chartone.pivot_table(index=[f'{sickness}'], values=['patient_id'], columns=['weight_bins'], aggfunc='count')
    an.reset_index(inplace=True)

    dataforchart = an.loc[an[f'{sickness}']==1].transpose()
    dataforchart.reset_index(inplace=True)
    
    values = dataforchart[1].sum()
    dataforchart.loc[(dataforchart[1]/values < 0.05),'weight_bins']='other'
    dataforchart = dataforchart.groupby(by='weight_bins').agg({1:'sum'})
    dataforchart.reset_index(inplace=True)
    dataforchart.loc[(dataforchart[1]== np.nan), 1] = 0
    
    #define data
    data = list(dataforchart[1])
    labels = list(dataforchart['weight_bins'])
    explode = [0.1 for x in labels]


    #define Seaborn color palette to use
    colors = sns.color_palette('pastel')[0:9]

    #create pie chart
    plt.pie(data,explode = explode, colors = colors, autopct='%.0f%%')
    plt.legend(labels, bbox_to_anchor=(1.2, 1.0), loc='upper left')
    return plt.show()


def height_pie_chart(sickness):  
    # code to create loop for input of streamlit user input
    chartone = survival[[f'{sickness}','height_bins','patient_id']]
    an = chartone.pivot_table(index=[f'{sickness}'], values=['patient_id'], columns=['height_bins'], aggfunc='count')
    an.reset_index(inplace=True)

    dataforchart = an.loc[an[f'{sickness}']==1].transpose()
    dataforchart.reset_index(inplace=True)
    
    values = dataforchart[1].sum()
    dataforchart.loc[(dataforchart[1]/values < 0.05),'height_bins']='other'
    dataforchart = dataforchart.groupby(by='height_bins').agg({1:'sum'})
    dataforchart.reset_index(inplace=True)
    dataforchart.loc[(dataforchart[1]== np.nan), 1] = 0
    
    #define data
    data = list(dataforchart[1])
    labels = list(dataforchart['height_bins'])
    explode = [0.1 for x in labels]


    #define Seaborn color palette to use
    colors = sns.color_palette('pastel')[0:9]

    #create pie chart
    plt.pie(data,explode = explode, colors = colors, autopct='%.0f%%')
    plt.legend(labels, bbox_to_anchor=(1.2, 1.0), loc='upper left')
    return plt.show()


def gender_sickness(sickness):
    
    charttwo = survival[[f'{sickness}','patient_id','gender_encoded']]

    an = charttwo.pivot_table(index=[f'{sickness}'], values=['patient_id'], columns=['gender_encoded'], aggfunc='count')
    an.reset_index(inplace=True)

    dataforchart = an[an[f'{sickness}']==1]
    dataforchart.rename(columns={0:'female',1:'male'}, inplace=True)

    del dataforchart[f'{sickness}']
    dataforchart=dataforchart.transpose()
    dataforchart.reset_index(inplace=True)

    sns.barplot(x='gender_encoded', y=1, data=dataforchart)
    plt.legend()
    return plt.show()


def death_sickness(sickness):
    
    charttwo = survival[[f'{sickness}','patient_id','hospital_death']]

    an = charttwo.pivot_table(index=[f'{sickness}'], values=['patient_id'], columns=['hospital_death'], aggfunc='count')
    an.reset_index(inplace=True)
    dataforchart = an[an[f'{sickness}']==1]
    dataforchart.rename(columns={0:'alive',1:'dead'}, inplace=True)
    
    del dataforchart[f'{sickness}']
    dataforchart=dataforchart.transpose()
    dataforchart.reset_index(inplace=True)

    sns.barplot(x='hospital_death', y=1, data=dataforchart)
    plt.legend()
    return plt.show()


option = st.selectbox(
     'What sickness would you like to see analyzed?',
     ('cirrhosis', 'aids', 'diabetes','hepatic_failure','immunosuppression','leukemia','lymphoma','solid_tumor_with_metastasis'))

st.write('You selected:', option)

diseases = ['cirrhosis', 'aids', 'diabetes','hepatic_failure','immunosuppression','leukemia','lymphoma','solid_tumor_with_metastasis']

for disease in diseases:
    if disease == option:
        st.header('the amount of cases that end in death ')       
        fig, ax = plt.subplots()
        ax = death_sickness(option)
        st.pyplot(fig)
        
        st.header(f'the gender distribution for {option}')       
        fig, ax = plt.subplots()
        ax = gender_sickness(option)
        st.pyplot(fig)
        
        st.header(f'the height(in cm) distribution for {option}')       
        fig, ax = plt.subplots()
        ax = height_pie_chart(option)
        st.pyplot(fig)
        
        st.header(f'the weight(in kg) distribution for {option}')       
        fig, ax = plt.subplots()
        ax = weight_pie_chart(option)
        st.pyplot(fig)

        st.header(f'the age distribution for {option}')       
        fig, ax = plt.subplots()
        ax = age_pie_chart(option)
        st.pyplot(fig)  






