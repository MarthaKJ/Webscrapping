import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.m.wikipedia.org/wiki/List_of_largest_law_firms_by_revenue"
#html content
response = requests.get(url)
html = response.content

#parsing the html content
parse = BeautifulSoup(html, "html.parser")

#table containing the list
table = parse.find("table", class_="wikitable")
#extracting data from the table
data = []
for row in table.find_all('tr')[1:]:
    row_data = [cell.text.strip() for cell in row.find_all(["th","td"])]
    data.append(row_data)
    print(data)

#convert the data into data frame
df = pd.DataFrame(data, columns=["Rank", "Firm", "Revenue (USD)","Lawyers", "Revenue per lawyer(US$)", "Profit per partner(US$)", "Country with the most lawyers"])
df = df.replace('', pd.NA)

#remove the rows with NaN
df = df.dropna(subset=["Rank"])
print(df)
