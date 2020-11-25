import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

#General variables
filename = "./data_clean.csv"

#storing data in df
df = pd.read_csv(filename)

#adding column of qualified or not
top_4 = ["Envy", "Sentinels", "100 Thieves", "Renegades"];
df["QUAL"] = df['TEAM']
df["QUAL"] = df["QUAL"].apply(lambda x : x in top_4)

#creating dataframe of data organized by team (average).
team_df = df
team_df = team_df.drop(columns=['PLAYER'])
team_df = team_df.groupby(['TEAM']).mean()
print(team_df)

#plots a column based on a boolean column.
def plot_one_column_bool(df, col_name, bool_col):
    a_plot_list = np.where(df[bool_col], df[col_name], None)
    b_plot_list = np.where(df[bool_col] != True, df[col_name], None)
    xaxis = pd.Series(list(range(len(df))))
    plt.scatter(x = xaxis, y = a_plot_list, label=bool_col + ": True")
    plt.scatter(x = xaxis, y = b_plot_list, label=bool_col + ": False")
    plt.ylabel(col_name)
    plt.legend(loc = 'upper left')
    plt.show()

#plots two columns against each other and gives line of best fit.
def plot_two_cols(df, col_x, col_y):
    plt.scatter(x = df[col_x], y = df[col_y])
    m, b = np.polyfit(df[col_x], df[col_y], 1)
    equation = str(round(m,2)) + 'x' ' + ' + str(round(b,2))
    plt.plot(df[col_x], m*df[col_x] + b, label = equation)
    plt.ylabel(col_y)
    plt.xlabel(col_x)
    plt.legend()
    plt.show()

#Preliminary plots
# plot_one_column_bool(df, "DPR", "QUAL")
# plot_two_cols(df, "DPR", "ESR")
# plot_two_cols(team_df, "DPR", "ACS")
# plot_two_cols(team_df, "ECON", "ACS")
# plot_two_cols(team_df, "ECON", "PL")
# plot_one_column_bool(team_df, "ACS", "QUAL")
# plot_one_column_bool(team_df, "DPR", "QUAL")
# plot_one_column_bool(team_df, "ESR", "QUAL")
# plot_one_column_bool(team_df, "HS%", "QUAL")
# plot_one_column_bool(team_df, "FB", "QUAL")
