#importing modules
import pandas as pd

#reading the clean data in
df_nsg = pd.read_csv("data_clean.csv")
df_umg = pd.read_csv("UMG_data_clean.csv")

#merging the data
df_merged = pd.concat([df_nsg, df_umg])

#print(df_merged) Test to see if merging worked.

df_merged.to_csv("./merged_data.csv")
