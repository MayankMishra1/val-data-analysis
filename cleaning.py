import pandas as pd
import numpy as np
import csv

#General variables
filename = "./data.csv"

#storing data in df
df = pd.read_csv(filename)

#seperating player and team data.
df['PLAYER'] = df['PLAYER'].apply(lambda x : x.strip('&'))
df["TEAM"] = df["PLAYER"].apply(lambda x : x.split('&'))
df["PLAYER"] = df["PLAYER"].apply(lambda x : x.split('&')[0])
df["TEAM"] = df["TEAM"].apply(lambda x : x[len(x)-1])

#Translating percentages into floats.
print(df.dtypes)
df['ESR'] = df['ESR'].apply(lambda x : x.strip('%'))
df["ESR"] = df["ESR"].astype(float)
df["ESR"] = df["ESR"].apply(lambda x : x/100.0)
df['HS%'] = df['HS%'].apply(lambda x : x.strip('%'))
df["HS%"] = df["HS%"].astype(float)
df["HS%"] = df["HS%"].apply(lambda x : x/100.0)

#Organizing Columns
df = df[["PLAYER","TEAM","ACS","ADR","K/D","K","D","A","RP","KPR","ESR","HS%","FBPR","DPR","1vX","MK","FB","FD","ECON","PL","DE"]]

#printing to ensure cleaning worked.
print(df.head())

#Writing to same CSV.
df.to_csv("./data_clean.csv", index = False, header=True)
