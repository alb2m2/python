"""
Created on Sat Apr  4 22:16:54 2020

@author: Alberto Matamoros
"""
#This is a script to filter the covid-19 data to show the cases in Honduras. The output is a .csv file. 

import pandas as pd
import matplotlib.pyplot as plt

# loading data right from the source:
death_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
recovered_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
country_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')

#filtering HND from raw data
death_HN_df=death_df[death_df['Country/Region']=='Honduras']
confirmed_HN_df=confirmed_df[confirmed_df['Country/Region']=='Honduras']
recovered_HN_df=recovered_df[recovered_df['Country/Region']=='Honduras']
country_HN_df=country_df[country_df['Country_Region']=='Honduras']

#merging the Honduran data into a single csv
frames=[confirmed_HN_df, recovered_HN_df, death_HN_df]
Honduras=pd.concat(frames)
descriptions=['Confirmed','Recovered','Death']
Honduras['Country/Region']=descriptions
Honduras.rename(columns={'Country/Region':'Status'})

#Saving data into a local file 
Honduras.to_csv('/home/alb2m2/Documents/HondurasResumen.csv')
