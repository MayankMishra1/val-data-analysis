# importing the libraries
from bs4 import BeautifulSoup
import requests
import csv

#General variables
url = "https://www.thespike.gg/events/stats/players/first-strike-north-america-nsg-tournament-closed-qualifier/248"
filename = "data.csv"

#HTTP Request
html = requests.get(url).text

#Parsing html page
soup = BeautifulSoup(html, "lxml")
#print(soup.prettify())

#getting table in plaintext
pstats_table = soup.find("table", attrs={"class": "player-stats"})

#storing headers.
t_headers = []
for th in pstats_table.find_all("th"):
    t_headers.append(th.text.replace('\n', ' ').strip())
#print(t_headers)

#storing player data in list of dictionaries
table_data = []
for tr in pstats_table.find_all("tr"):
    t_row = {}
    for td, th in zip(tr.find_all("td"), t_headers):
        t_row[th] = td.text.replace('\n', '').strip()
    table_data.append(t_row)
#print(table_data)

# exporting data to csv file.
keys = table_data[0].keys()
with open(filename, 'w', newline='') as csvfile:
    dict_writer = csv.DictWriter(csvfile, keys)
    dict_writer.writeheader()
    dict_writer.writerows(table_data)
