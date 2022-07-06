import requests
import pandas as pd

url = 'https://api.exchangerate.host/timeseries?start_date=2021-01-01&end_date=2021-01-10&base=USD'
response = requests.get(url)
data = response.json()

columns = ["date", "name", "value"]

data_frame = pd.DataFrame(columns=columns)

print(data_frame)

for date in data['rates']:
    for currency in data['rates'][date]:
        value = data['rates'][date][currency]
        new_row = [date, currency, value]
        data_frame.loc[len(data_frame)] = new_row

print(data_frame)